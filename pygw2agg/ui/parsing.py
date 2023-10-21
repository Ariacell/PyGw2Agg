import os
import subprocess
from PySimpleGUI import Button, popup_error_with_traceback, Window
import structlog

from pygw2agg.ui.settings import get_settings_path, get_user_settings
from pygw2agg.ui.table import AGGREGATE_TABLE_KEY, get_table

logger = structlog.get_logger("user_bar")


def get_user_bar_layout():
    return Button(button_text="Parse", key="-PARSE_BUTTON-")


def get_logs_from_directory(input_directory):
    res = []
    # Iterate directory
    for file in os.listdir(input_directory):
        # check only text files
        if file.endswith(".zevtc"):
            res.append(f"{input_directory}\{file}")
    return res


def handle_parse_event(window: Window, event, values):
    try:
        settings = get_user_settings(get_settings_path())
        logger.debug(f"Using settings: {settings}")

        exec_path = settings.get("-EI_EXEC_PATH-")
        input_path = settings.get("-INPUT_PATH-")
        if not exec_path or not input_path:
            missing_settings_warning_msg = (
                "Missing exec or input path, are your settings updated?"
            )
            logger.warn(missing_settings_warning_msg)
            raise Exception(missing_settings_warning_msg)
        output_path = settings.get("-OUTPUT_PATH-", input_path)

        config_path = f"{os.getcwd()}\\gw2ei_config.conf".replace("\\", "/")
        files_array = get_logs_from_directory(input_path)
        logger.info(
            f"Attempting to parse {len(files_array)} logs from directory at {input_path} using executable at {exec_path}"
        )
        args_array = [
            f"{exec_path}",
            "-c",
            f"{config_path}",
        ] + files_array
        logger.debug(f"Full command to run with args: {args_array}")
        subprocess.run(
            args_array,
            shell=True,
            text=True,
            capture_output=True,
        )
        logger.info("Parsing completed")
    except Exception as e:
        popup_error_with_traceback(f"Error while attempting to parse logs: {e}")

    headings = ["Name", "Class Mark", "Age", "Homeroom Class"]
    data = [
        ["Jason", 31, 15, "A"],
        ["John", 92, 16, "B"],
        ["Ann", 77, 17, "C"],
        ["Charlie", 18, 17, "D"],
        ["Sarah", 55, 14, "A"],
    ]
    window.extend_layout(window["-MAIN_COL-"], [get_table(data, headings)])
    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    # C:\Users\Aria\Desktop\Gw2\Logs\2023_05_14_DadLossLATE_Thief_15s
