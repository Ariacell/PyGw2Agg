import types
import PySimpleGUI as sg
import operator
from pygw2agg.models.aggregated.defense import (
    get_avg_damage_taken_friendly_name,
    get_avg_deaths_per_min_friendly_name,
    get_avg_dodge_count_friendly_name,
    get_avg_downs_per_min_friendly_name,
    get_total_damage_taken_friendly_name,
    get_total_deaths_friendly_name,
    get_total_dodge_count_friendly_name,
    get_total_times_downed_friendly_name,
)
from pygw2agg.models.aggregated.misc import active_time_friendly_name
from pygw2agg.models.aggregated.offense import (
    get_average_downed_contribution_friendly_name,
    get_average_dps_friendly_name,
    get_total_damage_friendly_name,
    get_total_downed_contribution_friendly_name,
)
from pygw2agg.models.aggregated.support import (
    get_average_cleanses_friendly_name,
    get_average_resurrect_time_friendly_name,
    get_average_resurrects_friendly_name,
    get_total_cleanses_friendly_name,
    get_total_resurrects_friendly_name,
)
from pygw2agg.models.aggregated.utility import (
    get_average_interrupts_friendly_name,
    get_average_strips_friendly_name,
    get_avg_comm_distance_friendly_name,
    get_avg_squad_distance_friendly_name,
    get_total_interrupts_friendly_name,
    get_total_rounds_friendly_name,
    get_total_strips_friendly_name,
)

# Use a 2D Array
sg.theme("Light green 6")


# table is a 2D array
# col_clicked is the column to sort by
def sort_table(table, col_clicked):
    try:
        # This takes the table and sorts everything given the column number (index)
        # Sorts table in place
        # operator.itemgetter returns column as an object
        table = sorted(table, key=operator.itemgetter(col_clicked))
    except Exception as e:
        sg.popup_error("Error in sort_table", "Exception in sort_table", e)
    return table


# ------ Window Layout ------
TABLE_KEYS = types.SimpleNamespace()

TABLE_KEYS.AGGREGATE_TABLE_KEY = "-AGGREGATE_TABLE-"
AGGREGATE_TABLE_SUMMARY_TAB_KEY = "-AGGREGATE_TABLE_TAB-SUMMARY"
TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY = "-AGGREGATE_TABLE-SUMMARY"
AGGREGATE_TABLE_DEFENSE_TAB_KEY = "-AGGREGATE_TABLE_TAB-DEFENSE"
TABLE_KEYS.AGGREGATE_TABLE_DEFENSE_KEY = "-AGGREGATE_TABLE-DEFENSE"
AGGREGATE_TABLE_OFFENSE_TAB_KEY = "-AGGREGATE_TABLE_TAB-OFFENSE"
TABLE_KEYS.AGGREGATE_TABLE_OFFENSE_KEY = "-AGGREGATE_TABLE-OFFENSE"
AGGREGATE_TABLE_UTILITY_TAB_KEY = "-AGGREGATE_TABLE_TAB-UTILTIY"
TABLE_KEYS.AGGREGATE_TABLE_UTILITY_KEY = "-AGGREGATE_TABLE-UTILITY"

AGGREGATE_TABLE_PSG_KEYS = [
    TABLE_KEYS.AGGREGATE_TABLE_KEY,
    AGGREGATE_TABLE_SUMMARY_TAB_KEY,
    TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY,
    AGGREGATE_TABLE_DEFENSE_TAB_KEY,
    TABLE_KEYS.AGGREGATE_TABLE_DEFENSE_KEY,
    AGGREGATE_TABLE_OFFENSE_TAB_KEY,
    TABLE_KEYS.AGGREGATE_TABLE_OFFENSE_KEY,
    AGGREGATE_TABLE_UTILITY_TAB_KEY,
    TABLE_KEYS.AGGREGATE_TABLE_UTILITY_KEY,
]

COMMON_HEADINGS = ["Name", "Account", "Profession"]


AGGREGATE_TABLE_SUMMARY_HEADINGS = [
    active_time_friendly_name,
    get_total_rounds_friendly_name(),
    get_average_dps_friendly_name(),
    get_average_downed_contribution_friendly_name(),
    get_avg_damage_taken_friendly_name(),
    get_average_cleanses_friendly_name(),
    get_average_strips_friendly_name(),
    get_average_interrupts_friendly_name(),
    get_avg_downs_per_min_friendly_name(),
    get_avg_deaths_per_min_friendly_name(),
]
MERGED_AGGREGATE_TABLE_SUMMARY_HEADINGS = (
    COMMON_HEADINGS + AGGREGATE_TABLE_SUMMARY_HEADINGS
)
AGGREGATE_TABLE_DEFENSE_HEADINGS = [
    get_total_cleanses_friendly_name(),
    get_average_cleanses_friendly_name(),
    get_total_resurrects_friendly_name(),
    get_average_resurrects_friendly_name(),
    get_average_resurrect_time_friendly_name(),
    get_total_dodge_count_friendly_name(),
    get_avg_dodge_count_friendly_name(),
    get_total_damage_taken_friendly_name(),
    get_avg_damage_taken_friendly_name(),
    get_total_times_downed_friendly_name(),
    get_avg_downs_per_min_friendly_name(),
    get_total_deaths_friendly_name(),
    get_avg_deaths_per_min_friendly_name(),
]
MERGED_AGGREGATE_TABLE_DEFENSE_HEADINGS = (
    COMMON_HEADINGS + AGGREGATE_TABLE_DEFENSE_HEADINGS
)
AGGREGATE_TABLE_OFFENSE_HEADINGS = [
    get_total_downed_contribution_friendly_name(),
    get_total_damage_friendly_name(),
    get_average_dps_friendly_name(),
    get_average_downed_contribution_friendly_name(),
]
MERGED_AGGREGATE_TABLE_OFFENSE_HEADINGS = (
    COMMON_HEADINGS + AGGREGATE_TABLE_OFFENSE_HEADINGS
)
AGGREGATE_TABLE_UTILITY_HEADINGS = [
    get_total_strips_friendly_name(),
    get_average_strips_friendly_name(),
    get_total_interrupts_friendly_name(),
    get_average_interrupts_friendly_name(),
    get_avg_squad_distance_friendly_name(),
    get_avg_comm_distance_friendly_name(),
]
MERGED_AGGREGATE_TABLE_UTILITY_HEADINGS = (
    COMMON_HEADINGS + AGGREGATE_TABLE_UTILITY_HEADINGS
)


def get_table(data, visible):
    return (
        sg.TabGroup(
            [
                [
                    sg.Tab(
                        "Basic Info",
                        [
                            [
                                sg.Table(
                                    values=data,
                                    headings=MERGED_AGGREGATE_TABLE_SUMMARY_HEADINGS,
                                    max_col_width=20,
                                    auto_size_columns=True,
                                    display_row_numbers=False,
                                    justification="right",
                                    num_rows=20,
                                    expand_x=True,
                                    expand_y=True,
                                    alternating_row_color="lightyellow",
                                    key=TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY,
                                    enable_events=True,
                                    enable_click_events=True,  # Comment out to not enable header and other clicks
                                    tooltip="Main summary table with general information",
                                    visible=visible,
                                    vertical_scroll_only=False,
                                )
                            ]
                        ],
                        visible=visible,
                        key=AGGREGATE_TABLE_SUMMARY_TAB_KEY,
                    ),
                    sg.Tab(
                        "Defense",
                        [
                            [
                                sg.Table(
                                    values=data,
                                    headings=MERGED_AGGREGATE_TABLE_DEFENSE_HEADINGS,
                                    max_col_width=20,
                                    auto_size_columns=True,
                                    display_row_numbers=False,
                                    justification="right",
                                    num_rows=20,
                                    expand_x=True,
                                    expand_y=True,
                                    alternating_row_color="lightyellow",
                                    key=TABLE_KEYS.AGGREGATE_TABLE_DEFENSE_KEY,
                                    enable_events=True,
                                    enable_click_events=True,  # Comment out to not enable header and other clicks
                                    tooltip="Main summary table with general information",
                                    visible=visible,
                                    vertical_scroll_only=False,
                                )
                            ]
                        ],
                        visible=visible,
                        key=AGGREGATE_TABLE_DEFENSE_TAB_KEY,
                    ),
                    sg.Tab(
                        "Offense",
                        [
                            [
                                sg.Table(
                                    values=data,
                                    headings=MERGED_AGGREGATE_TABLE_OFFENSE_HEADINGS,
                                    max_col_width=20,
                                    auto_size_columns=True,
                                    display_row_numbers=False,
                                    justification="right",
                                    num_rows=20,
                                    expand_x=True,
                                    expand_y=True,
                                    alternating_row_color="lightyellow",
                                    key=TABLE_KEYS.AGGREGATE_TABLE_OFFENSE_KEY,
                                    enable_events=True,
                                    enable_click_events=True,  # Comment out to not enable header and other clicks
                                    tooltip="Main summary table with general information",
                                    visible=visible,
                                    vertical_scroll_only=False,
                                )
                            ]
                        ],
                        visible=visible,
                        key=AGGREGATE_TABLE_OFFENSE_TAB_KEY,
                    ),
                    sg.Tab(
                        "Utility",
                        [
                            [
                                sg.Table(
                                    values=data,
                                    headings=MERGED_AGGREGATE_TABLE_UTILITY_HEADINGS,
                                    max_col_width=20,
                                    auto_size_columns=True,
                                    display_row_numbers=False,
                                    justification="right",
                                    num_rows=20,
                                    expand_x=True,
                                    expand_y=True,
                                    alternating_row_color="lightyellow",
                                    key=TABLE_KEYS.AGGREGATE_TABLE_UTILITY_KEY,
                                    enable_events=True,
                                    enable_click_events=True,  # Comment out to not enable header and other clicks
                                    tooltip="Main summary table with general information",
                                    visible=visible,
                                    vertical_scroll_only=False,
                                )
                            ]
                        ],
                        visible=visible,
                        key=AGGREGATE_TABLE_UTILITY_TAB_KEY,
                    ),
                ]
            ],
            key=TABLE_KEYS.AGGREGATE_TABLE_KEY,
            visible=visible,
            expand_x=True,
            expand_y=True,
        ),
    )


def handle_table_event(event, window, data):
    if (
        event[2][0] == -1 and event[2][1] != -1
    ):  # Header was clicked and wasn't the "row" column
        col_num_clicked = event[2][1]
        match event[0]:
            case TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY:
                new_table = sort_table(data.summary, col_num_clicked)
                window[TABLE_KEYS.AGGREGATE_TABLE_SUMMARY_KEY].update(new_table)
            case TABLE_KEYS.AGGREGATE_TABLE_OFFENSE_KEY:
                new_table = sort_table(data.offense, col_num_clicked)
                window[TABLE_KEYS.AGGREGATE_TABLE_OFFENSE_KEY].update(new_table)
            case TABLE_KEYS.AGGREGATE_TABLE_DEFENSE_KEY:
                new_table = sort_table(data.defense, col_num_clicked)
                window[TABLE_KEYS.AGGREGATE_TABLE_DEFENSE_KEY].update(new_table)
            case TABLE_KEYS.AGGREGATE_TABLE_UTILITY_KEY:
                new_table = sort_table(data.utility, col_num_clicked)
                window[TABLE_KEYS.AGGREGATE_TABLE_UTILITY_KEY].update(new_table)
            case _:
                print("Unknown table key")
