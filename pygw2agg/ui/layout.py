from pygw2agg.ui.menu_bar import get_menu_bar_layout
from pygw2agg.ui.parsing import (
    AGGREGATING_IN_PROGRESS_KEY,
    PARSING_IN_PROGRESS_KEY,
    get_parsing_options_layout,
    get_progress_info_button,
)

from pygw2agg.ui.table import get_table
from PySimpleGUI import Col, VerticalSeparator, Text, pin


def get_layout():
    return [
        [
            pin(
                Col(
                    [
                        [get_menu_bar_layout()],
                        get_parsing_options_layout(),
                        [
                            get_progress_info_button(
                                "Parsing .zevtc logs...",
                                PARSING_IN_PROGRESS_KEY,
                                visible=False,
                            )
                        ],
                        [
                            get_progress_info_button(
                                "Aggregating JSON logs...",
                                AGGREGATING_IN_PROGRESS_KEY,
                                visible=False,
                            )
                        ],
                        get_table([], visible=False),
                    ],
                    key="-MAIN_COL-",
                    expand_x=True,
                    expand_y=True,
                )
            ),
            VerticalSeparator(),
            Col(
                [[Text("Utilities")]],
                key="-SIDE_COL-",
                background_color="teal",
            ),
        ]
    ]
