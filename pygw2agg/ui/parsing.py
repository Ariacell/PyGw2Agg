import os
from typing import List
from PySimpleGUI import (
    Button,
    popup_error_with_traceback,
    Window,
    Text,
    InputText,
    FolderBrowse,
)
import traceback
import structlog
from pygw2agg.io.generate_index import generate_index_html
from pygw2agg.io.load_json import load_json
from pygw2agg.io.parse import parse_zevtc_logs_to_json
from pygw2agg.logic.main import aggregate_player_log_data, get_aggregate_metadata
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.settings_keys import INPUT_DIRECTORY_KEY
from pygw2agg.ui.mapping import map_aggregated_data_to_table_structure

from pygw2agg.ui.settings import get_settings_path, get_user_settings
from pygw2agg.ui.table import (
    AGGREGATE_TABLE_PSG_KEYS,
    AGGREGATE_TABLE_SUMMARY_TAB_KEY,
    TABLE_KEYS,
)
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


def toggle_table_display(window, visible):
    for key in AGGREGATE_TABLE_PSG_KEYS:
        window[key].update(visible=visible)
    if visible == True:
        window[AGGREGATE_TABLE_SUMMARY_TAB_KEY].select()


def reset_table_values(window):
    window[TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY].update(values=[])


def handle_parse_event(window: Window, event, values):
    try:
        toggle_table_display(window, False)
        reset_table_values(window)
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

        validated_json_data = load_json(json_log_paths)
        aggregated_player_data = aggregate_player_log_data(validated_json_data)
        aggregated_metadata = get_aggregate_metadata(validated_json_data)
        # Table data should have it's own tranformation in logic/model module, aggregation is a logic step, mapping to ui representation is a domain model responsibility imo.
        ui_table_data = map_aggregated_data_to_table_structure(
            aggregated_data=aggregated_player_data
        )
        logger.debug(f"Mapped aggregated data to table structure: {ui_table_data}")
        window[TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY].update(
            values=ui_table_data.summary
        )
        window[TABLE_KEYS.AGGREGATE_TABLE_DEFENSE_KEY].update(
            values=ui_table_data.defense
        )
        window[TABLE_KEYS.AGGREGATE_TABLE_OFFENSE_KEY].update(
            values=ui_table_data.offense
        )
        window[TABLE_KEYS.AGGREGATE_TABLE_UTILITY_KEY].update(
            values=ui_table_data.utility
        )
        toggle_table_display(window, True)
        generate_index_html(
            aggregated_metadata=aggregated_metadata,
            aggregated_player_data=aggregate_player_log_data,
        )
        return ui_table_data
    except Exception as e:
        traceback.print_exc()
        popup_error_with_traceback(f"Error while attempting to aggregate logs: {e}")
    finally:
        window[AGGREGATING_IN_PROGRESS_KEY].update(visible=False)
        window.refresh()

    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    # C:\Users\Aria\Desktop\Gw2\Logs\2023_05_14_DadLossLATE_Thief_15s
