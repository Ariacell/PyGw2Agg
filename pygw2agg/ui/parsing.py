from PySimpleGUI import (
    Button,
    popup_error_with_traceback,
    Window,
    Text,
    InputText,
    FolderBrowse,
)
import structlog
from pygw2agg.io.load_json import load_json
from pygw2agg.io.parse import parse_zevtc_logs_to_json
from pygw2agg.settings_keys import INPUT_DIRECTORY_KEY

from pygw2agg.ui.settings import get_settings_path, get_user_settings
from pygw2agg.ui.table import AGGREGATE_TABLE_KEY
from pygw2agg.ui.utils import (
    get_working_directory,
)

logger = structlog.get_logger("user_bar")



INPUT_DIRECTORY_TOOLTIP = "The fully qualified path to your input directory containing .zevtc files to parse and aggregate"


def get_parsing_options_layout():
    return [
        Text("Please select input directory:", tooltip=INPUT_DIRECTORY_TOOLTIP),
        InputText(
            key=INPUT_DIRECTORY_KEY, tooltip=INPUT_DIRECTORY_TOOLTIP, enable_events=True
        ),
        FolderBrowse(
            initial_folder=get_working_directory(),
            tooltip=INPUT_DIRECTORY_TOOLTIP,
            key=INPUT_DIRECTORY_KEY,
            enable_events="True",
        ),
        Button(
            button_text="Parse",
            key="-PARSE_BUTTON-",
            tooltip="Parse and aggregate a collection of logs from your input directory",
        ),
    ]


PARSING_IN_PROGRESS_KEY = "-PARSING_IN_PROGRESS_TEXT-"
AGGREGATING_IN_PROGRESS_KEY = "-AGGREGATING_IN_PROGRESS_TEXT-"


def handle_input_path_event(window, event, values):
    settings = get_user_settings()
    settings.set(INPUT_DIRECTORY_KEY, values[INPUT_DIRECTORY_KEY])


def get_progress_info_button(current_operation: str, key, visible):
    return Text(current_operation, key=key, visible=visible)


def handle_parse_event(window: Window, event, values):
    try:
        window[AGGREGATE_TABLE_KEY].update(visible=False)
        window[PARSING_IN_PROGRESS_KEY].update(visible=True)
        window.refresh()
        settings = get_user_settings(get_settings_path())
        logger.debug(f"Using settings: {settings}")

        json_log_paths = parse_zevtc_logs_to_json(settings)
    except Exception as e:
        popup_error_with_traceback(f"Error while attempting to parse logs: {e}")
    finally:
        window[PARSING_IN_PROGRESS_KEY].update(visible=False)
        window.refresh()

    try:
        window[AGGREGATING_IN_PROGRESS_KEY].update(visible=True)
        window.refresh()
        load_json(json_log_paths)

        data = [
            ["Jason", 31, 15, "A"],
            ["John", 92, 16, "B"],
            ["Ann", 77, 17, "C"],
            ["Charlie", 18, 17, "D"],
            ["Sarah", 55, 14, "A"],
        ]
        window[AGGREGATE_TABLE_KEY].update(visible=True, values=data)
        return data
    except Exception as e:
        popup_error_with_traceback(f"Error while attempting to aggregate logs: {e}")
    finally:
        window[AGGREGATING_IN_PROGRESS_KEY].update(visible=False)
        window.refresh()
    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    # C:\Users\Aria\Desktop\Gw2\Logs\2023_05_14_DadLossLATE_Thief_15s
