from pygw2agg.ui.menu_bar import (
    get_EI_exec_path_layout,
    get_filepath_section,
    get_menu_bar,
)
from PySimpleGUI import Table

from pygw2agg.ui.table import get_table
from pygw2agg.ui.user_bar import get_user_bar_layout


def get_layout(data, headings):
    return [
        [
            get_menu_bar(),
            get_EI_exec_path_layout(),
            get_filepath_section(),
            get_user_bar_layout(),
            get_table(data, headings),
        ]
    ]
