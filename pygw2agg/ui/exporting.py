import csv
from os import path
from typing import List
from PySimpleGUI import Button, Text, Window, WIN_CLOSED, Table
import structlog
from pygw2agg.settings_keys import OUTPUT_DIRECTORY_KEY

from pygw2agg.ui.settings import get_user_settings

logger = structlog.get_logger("exporting")


def handle_export_menu_event(event, values, tables):
    if event == "Export":
        open_settings(tables)


def get_export_menu_layout():
    return [
        [Text("Choose table to export", justification="left")],
        [Button("Export Basic Info"), Button("Exit")],
    ]


# Event Loop
def open_settings(tables: List[Table]):
    window = Window("User Settings Demo", get_export_menu_layout())

    while True:
        event, values = window.read()
        if event in (WIN_CLOSED, "Exit"):
            break
        if event == "Export Basic Info":
            settings = get_user_settings()
            output_directory = settings.get(OUTPUT_DIRECTORY_KEY)
            print(f"exporting tables info as CSVs to output path {output_directory}")
            for table in tables:
                filename = f"{table.Key}.csv"
                output_path = path.join(output_directory, filename)
                with open(output_path, "w", newline="") as f:
                    writer = csv.writer(
                        f,
                    )
                    data = [table.ColumnHeadings] + [value for value in table.Values]
                    writer.writerows(data)
                    logger.info(f"Wrote csv file to {output_path}")
            break
    window.close()
