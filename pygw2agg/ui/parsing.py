import os
import subprocess
import time
from PySimpleGUI import Button, popup_error_with_traceback, Window, Text
import structlog
from pygw2agg.io.parse import parse_zevtc_logs_to_json

from pygw2agg.ui.settings import get_settings_path, get_user_settings
from pygw2agg.ui.table import AGGREGATE_TABLE_KEY, get_table
from pygw2agg.ui.utils import remove_element, simple_extend_element

logger = structlog.get_logger("user_bar")


def get_user_bar_layout():
    return Button(button_text="Parse", key="-PARSE_BUTTON-")


PARSING_IN_PROGRESS_KEY = "-PARSING_IN_PROGRESS_TEXT-"
AGGREGATING_IN_PROGRESS_KEY = "-AGGREGATING_IN_PROGRESS_TEXT-"


def get_progress_info_button(current_operation: str, key):
    return Text(current_operation, key=key, visible=True)


def handle_parse_event(window: Window, event, values):
    try:
        simple_extend_element(
            window,
            get_progress_info_button("Parsing .zevtc logs...", PARSING_IN_PROGRESS_KEY),
        )
        settings = get_user_settings(get_settings_path())
        logger.debug(f"Using settings: {settings}")

        exec_path = settings.get("-EI_EXEC_PATH-")
        input_path = settings.get("-INPUT_PATH-")
        output_path = settings.get("-OUTPUT_PATH-")
        parse_zevtc_logs_to_json(
            exec_path=exec_path, input_path=input_path, output_path=output_path
        )
    except Exception as e:
        popup_error_with_traceback(f"Error while attempting to parse logs: {e}")
    finally:
        remove_element(window, PARSING_IN_PROGRESS_KEY)

    try:
        simple_extend_element(
            window,
            get_progress_info_button(
                "Aggregating JSON logs...", AGGREGATING_IN_PROGRESS_KEY
            ),
        )

        time.sleep(5)
        headings = ["Name", "Class Mark", "Age", "Homeroom Class"]
        data = [
            ["Jason", 31, 15, "A"],
            ["John", 92, 16, "B"],
            ["Ann", 77, 17, "C"],
            ["Charlie", 18, 17, "D"],
            ["Sarah", 55, 14, "A"],
        ]

        window.extend_layout(window["-MAIN_COL-"], [get_table(data, headings)])
        return data
    except Exception as e:
        popup_error_with_traceback(f"Error while attempting to parse logs: {e}")
    finally:
        remove_element(window, AGGREGATING_IN_PROGRESS_KEY)
    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    # C:\Users\Aria\Desktop\Gw2\Logs\2023_05_14_DadLossLATE_Thief_15s
