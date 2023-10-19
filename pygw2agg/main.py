import PySimpleGUI as sg
from pygw2agg.ui.layout import get_layout

from pygw2agg.ui.table import handle_table_event
from pygw2agg.ui.user_bar import handle_parse_event

headings = ["Name", "Class Mark", "Age", "Homeroom Class"]
data = [
    ["Jason", 31, 15, "A"],
    ["John", 92, 16, "B"],
    ["Ann", 77, 17, "C"],
    ["Charlie", 18, 17, "D"],
    ["Sarah", 55, 14, "A"],
]
# ------ Create Window ------
window = sg.Window(
    "The Table Element", get_layout(data, headings), ttk_theme="clam", resizable=True
)


# ------ Event Loop ------
def display_table():
    while True:
        event, values = window.read()
        print(event, values)
        print(event)
        if event == sg.WIN_CLOSED:
            break
        # If there's an event with a tuple, which can only a table will generate
        if isinstance(event, tuple):
            # TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
            if event[0] == "-TABLE-":
                # event[2][0] is the row
                # event[2][1] is the colum
                # If sure makes sure it's the statement and not the first column
                handle_table_event(event, window=window, data=data)
        if event == "-PARSE_BUTTON-":
            handle_parse_event(event, values)
    window.close()


display_table()
