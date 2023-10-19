import os
from PySimpleGUI import Menu, Text, InputText, FolderBrowse, FileBrowse

menu_def = [
    [
        "Memu1",
        [
            "btn1",
            "btn2",
            "btn3",
            "btn4",
        ],
    ],
    [
        "menu2",
        ["btn5", "btn6", "btn7", "btn8"],
    ],
]


def get_menu_bar():
    return Menu(menu_def)


working_directory = os.getcwd()


def get_EI_exec_path_layout():
    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    return [
        [Text("Please select the full path to your Elite Insights parser executable")],
        [InputText(key="-EI_EXEC_PATH-"), FileBrowse(initial_folder=working_directory)],
    ]


def get_filepath_section():
    return [
        [Text("Please select input directory:")],
        [InputText(key="-INPUT_PATH-"), FolderBrowse(initial_folder=working_directory)],
    ]
