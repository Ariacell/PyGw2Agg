import os
import subprocess
import time
from PySimpleGUI import Button, popup_error_with_traceback, Window, Text
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


PARSING_IN_PROGRESS_KEY = "-PARSING_IN_PROGRESS_TEXT-"
AGGREGATING_IN_PROGRESS_KEY = "-AGGREGATING_IN_PROGRESS_TEXT-"


def get_progress_info_button(current_operation: str, key):
    return Text(current_operation, key=key, visible=True)


def handle_parse_event(window: Window, event, values):
    try:
        window.extend_layout(
            window,
            [
                [
                    get_progress_info_button(
                        "Parsing .zevtc logs...", PARSING_IN_PROGRESS_KEY
                    )
                ]
            ],
        )
        window.refresh()
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

    window[PARSING_IN_PROGRESS_KEY].update(visible=False)
    window[PARSING_IN_PROGRESS_KEY].Widget.master.pack_forget()
    try:
        window.extend_layout(
            window,
            [
                [
                    get_progress_info_button(
                        "Aggregating JSON logs...", AGGREGATING_IN_PROGRESS_KEY
                    )
                ]
            ],
        )
        window.refresh()
        time.sleep(5)
        headings = ["Name", "Class Mark", "Age", "Homeroom Class"]
        data = [
            ["Jason", 31, 15, "A"],
            ["John", 92, 16, "B"],
            ["Ann", 77, 17, "C"],
            ["Charlie", 18, 17, "D"],
            ["Sarah", 55, 14, "A"],
        ]

        window[AGGREGATING_IN_PROGRESS_KEY].update(visible=False)
        window[AGGREGATING_IN_PROGRESS_KEY].Widget.master.pack_forget()
        window.extend_layout(window["-MAIN_COL-"], [get_table(data, headings)])
    except Exception as e:
        popup_error_with_traceback(f"Error while attempting to parse logs: {e}")

    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    # C:\Users\Aria\Desktop\Gw2\Logs\2023_05_14_DadLossLATE_Thief_15s
