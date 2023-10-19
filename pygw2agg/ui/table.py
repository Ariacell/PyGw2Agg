import PySimpleGUI as sg
import random
import string
import operator

from pygw2agg.ui.menu_bar import get_menu_bar

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
def get_table(data, headings):
    return (
        sg.Table(
            values=data,
            headings=headings,
            max_col_width=25,
            auto_size_columns=True,
            display_row_numbers=True,
            justification="right",
            num_rows=20,
            alternating_row_color="lightyellow",
            key="-TABLE-",
            enable_events=True,
            expand_x=True,
            expand_y=True,
            enable_click_events=True,  # Comment out to not enable header and other clicks
            tooltip="This is a table",
        ),
    )


def handle_table_event(event, window, data):
    if (
        event[2][0] == -1 and event[2][1] != -1
    ):  # Header was clicked and wasn't the "row" column
        col_num_clicked = event[2][1]
        new_table = sort_table(data, col_num_clicked)
        window["-TABLE-"].update(new_table)
