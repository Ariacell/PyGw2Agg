import os
from PySimpleGUI import Window
import structlog

logger = structlog.get_logger("UI_utils")


def simple_extend_element(window: Window, element):
    window.extend_layout(
        window,
        [[element]],
    )
    window.refresh()


def remove_element(window: Window, key: str):
    try:
        if window.find_element(key):
            window[key].update(visible=False)
    except:
        logger.warn("Swallowed error related to removing element")


def get_working_directory():
    os.getcwd()
