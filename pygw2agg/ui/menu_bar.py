from PySimpleGUI import Menu

menu_def = [
    [
        "File",
        ["Settings", "Export"],
    ],
]


def get_menu_bar_layout():
    return Menu(menu_def)
