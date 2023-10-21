from pygw2agg.ui.menu_bar import get_menu_bar_layout
from pygw2agg.ui.parsing import get_user_bar_layout

from pygw2agg.ui.table import get_table
from PySimpleGUI import Col


def get_layout():
    return [
        [
            Col(
                [
                    [get_menu_bar_layout()],
                    [get_user_bar_layout()],
                ],
                key="-MAIN_COL-",
            )
        ]
    ]
