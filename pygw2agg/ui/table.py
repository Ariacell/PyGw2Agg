import PySimpleGUI as sg
import operator


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
AGGREGATE_TABLE_KEY = "-AGGREGATE_TABLE-"
AGGREGATE_TABLE_SUMMARY_TAB_KEY = "-AGGREGATE_TABLE_TAB-SUMMARY"
AGGREGATE_TABLE_SUMMARY_KEY = "-AGGREGATE_TABLE-SUMMARY"
AGGREGATE_TABLE_DEFENSE_TAB_KEY = "-AGGREGATE_TABLE_TAB-DEFENSE"
AGGREGATE_TABLE_DEFENSE_KEY = "-AGGREGATE_TABLE-DEFENSE"

AGGREGATE_TABLE_PSG_KEYS = [
    AGGREGATE_TABLE_KEY,
    AGGREGATE_TABLE_SUMMARY_TAB_KEY,
    AGGREGATE_TABLE_SUMMARY_KEY,
    AGGREGATE_TABLE_DEFENSE_TAB_KEY,
    AGGREGATE_TABLE_DEFENSE_KEY,
]

COMMON_HEADINGS = ["Name", "Account", "Profession"]


AGGREGATE_TABLE_SUMMARY_HEADINGS = ["Ressurects"]
MERGED_AGGREGATE_TABLE_SUMMARY_HEADINGS = COMMON_HEADINGS + ["Ressurects"]
AGGREGATE_TABLE_DEFENSE_HEADINGS = ["Resurrect Time"]
MERGED_AGGREGATE_TABLE_DEFENSE_HEADINGS = COMMON_HEADINGS + ["Resurrect Time"]


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
                                    max_col_width=50,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification="right",
                                    num_rows=20,
                                    expand_x=True,
                                    expand_y=True,
                                    alternating_row_color="lightyellow",
                                    key=AGGREGATE_TABLE_SUMMARY_KEY,
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
                                    max_col_width=50,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification="right",
                                    num_rows=20,
                                    expand_x=True,
                                    expand_y=True,
                                    alternating_row_color="lightyellow",
                                    key=AGGREGATE_TABLE_DEFENSE_KEY,
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
                ]
            ],
            key=AGGREGATE_TABLE_KEY,
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
        new_table = sort_table(data, col_num_clicked)
        print(new_table)
        window[AGGREGATE_TABLE_SUMMARY_KEY].update(new_table)
