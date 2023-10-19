import glob
from os.path import isfile, join
import os
import subprocess
from PySimpleGUI import Button
import structlog

logger = structlog.get_logger("user_bar")


def get_user_bar_layout():
    return [[Button(button_text="Parse", key="-PARSE_BUTTON-")]]


def get_logs_from_directory(input_directory):
    res = []
    # Iterate directory
    for file in os.listdir(input_directory):
        # check only text files
        if file.endswith(".zevtc"):
            res.append(f"{input_directory}\{file}")
    return res


def handle_parse_event(event, values):
    input_path = values["-INPUT_PATH-"]
    exec_path = values["-EI_EXEC_PATH-"]
    config_path = f"{os.getcwd()}\\gw2ei_config.conf".replace("\\", "/")
    files_array = get_logs_from_directory(input_path)
    logger.info(
        f"Attempting to parse {len(files_array)} lgos from directory at {input_path} using executable at {exec_path}"
    )
    args_array = [
        f"{exec_path}",
        "-c",
        f"{config_path}",
    ] + files_array
    logger.debug(f"Full command to run with args: {args_array}")
    subprocess.run(
        args_array,
        shell=True,
        text=True,
        capture_output=True,
    )
    logger.info("Subprocess finished")

    # C:/Users/Aria/Desktop/Gw2/dev/GW2EI_Release/GuildWars2EliteInsights.exe
    # C:\Users\Aria\Desktop\Gw2\Logs\2023_05_14_DadLossLATE_Thief_15s
