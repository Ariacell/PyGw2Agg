import os
import PySimpleGUI as sg
import os
from PySimpleGUI import Text, InputText, FolderBrowse, FileBrowse
import structlog

from pygw2agg.ui.utils import get_working_directory

sg.set_options(font=("Arial Bold", 16))

logger = structlog.get_logger("settings")


def get_settings_path():
    return f"{os.getcwd()}/settings.txt"


def get_user_settings(path=get_settings_path()):
    if os.path.isfile(path):
        logger.info(f"Found settings file at {path}!")
        settings = sg.UserSettings(
            filename=get_settings_path(),
        )
    else:
        logger.info(
            "No settings file found, instantiating user settings using path: {path}"
        )
        settings = sg.UserSettings(filename=path)
    return settings


def handle_file_menu_event(event, values):
    if event == "Settings":
        open_settings()


EI_EXEC_PATH_KEY = "-EI_EXEC_PATH-"
EI_EXEC_PATH_TOOLTIP = "The fully qualified path to your executable Elite Insights exe, e.g. C://Users/Documents/GuildWars2EliteInsights.exe"


def get_EI_exec_path_layout():
    return [
        [
            Text(
                "Please select the full path to your Elite Insights parser executable",
                tooltip=EI_EXEC_PATH_TOOLTIP,
            )
        ],
        [
            InputText(
                key=EI_EXEC_PATH_KEY,
                tooltip=EI_EXEC_PATH_TOOLTIP,
            ),
            FileBrowse(
                initial_folder=get_working_directory(),
                tooltip=EI_EXEC_PATH_TOOLTIP,
            ),
        ],
    ]


OUTPUT_DIRECTORY_KEY = "-OUTPUT_PATH-"
OUTPUT_DIRECTORY_TOOLTIP = "If you would like to save output to a custom directory update this setting. Defaults to input directory."


def get_output_filepath_section():
    return [
        [Text("Please select output directory:", tooltip=OUTPUT_DIRECTORY_TOOLTIP)],
        [
            InputText(key=OUTPUT_DIRECTORY_KEY, tooltip=OUTPUT_DIRECTORY_TOOLTIP),
            FolderBrowse(
                initial_folder=get_working_directory(), tooltip=OUTPUT_DIRECTORY_TOOLTIP
            ),
        ],
    ]


def get_settings_layout():
    return [
        [sg.Text("Settings", justification="left")],
        get_EI_exec_path_layout(),
        get_output_filepath_section(),
        [sg.Button("LOAD"), sg.Button("SAVE"), sg.Button("Exit")],
    ]


# Event Loop
def open_settings():
    window = sg.Window("User Settings Demo", get_settings_layout())

    settings = sg.UserSettings()
    if os.path.isfile(get_settings_path()):
        print("Found settings file!")
        settings = sg.UserSettings(
            filename=get_settings_path(),
        )
    print(settings)
    while True:
        event, values = window.read()
        print(f"Settings: {settings}")
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "LOAD":
            window[EI_EXEC_PATH_KEY].update(value=settings[EI_EXEC_PATH_KEY])
            window[OUTPUT_DIRECTORY_KEY].update(value=settings[OUTPUT_DIRECTORY_KEY])
        if event == "SAVE":
            settings.set(EI_EXEC_PATH_KEY, values[EI_EXEC_PATH_KEY])
            settings.set(OUTPUT_DIRECTORY_KEY, values[OUTPUT_DIRECTORY_KEY])
            settings.save(get_settings_path())
    window.close()
