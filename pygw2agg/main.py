import PySimpleGUI as sg
import structlog
from pygw2agg.settings_keys import INPUT_DIRECTORY_KEY
from pygw2agg.ui.layout import get_layout
from pygw2agg.ui.parsing import (
    handle_input_path_event,
    handle_parse_event,
)
from pygw2agg.ui.settings import (
    get_user_settings,
    handle_file_menu_event,
)

from pygw2agg.ui.table import (
    AGGREGATE_TABLE_KEY,
    AGGREGATE_TABLE_SUMMARY_TAB_KEY,
    handle_table_event,
)

# ------ Create Window ------
window = sg.Window(
    "Main Window",
    get_layout(),
    return_keyboard_events=True,
    ttk_theme="classic",
    resizable=True,
    size=(1200, 800),
    finalize=True,
)
# Manually hide first tab after window initialisation, see https://github.com/PySimpleGUI/PySimpleGUI/issues/5837
window[AGGREGATE_TABLE_SUMMARY_TAB_KEY].update(visible=False)

logger = structlog.get_logger("main")


# ------ Event Loop ------
def display_table():
    settings = get_user_settings()
    AGGREGATE_DATA = None
    logger.info(f"Instantiated application with settings: {settings}")
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        # If there's an event with a tuple, which can only a table will generate
        if isinstance(event, tuple):
            # TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
            if event[0] == AGGREGATE_TABLE_KEY:
                # event[2][0] is the row
                # event[2][1] is the colum
                # If sure makes sure it's the statement and not the first column
                handle_table_event(event, window=window, data=AGGREGATE_DATA)
        if isinstance(event, str):
            if event == "-PARSE_BUTTON-":
                AGGREGATE_DATA = handle_parse_event(window, event, values)
                logger.debug(f"Aggregated data: {AGGREGATE_DATA}")
            if event == INPUT_DIRECTORY_KEY:
                handle_input_path_event(window, event, values)
            if event == "Settings":
                handle_file_menu_event(event, values)
    window.close()


display_table()
