import os
import subprocess
import structlog
from PySimpleGUI import UserSettings
from pygw2agg.settings_keys import (
    INPUT_DIRECTORY_KEY,
    EI_EXEC_PATH_KEY,
    OUTPUT_DIRECTORY_KEY,
)


logger = structlog.get_logger("io_parsing")


def get_logs_from_directory(input_directory):
    res = []
    # Iterate directory
    for file in os.listdir(input_directory):
        # check only text files
        if file.endswith(".zevtc"):
            res.append(f"{input_directory}\{file}")
    return res


def get_json_paths(output_directory):
    res = []
    # Iterate directory
    for file in os.listdir(output_directory):
        # check only text files
        if file.endswith(".json"):
            res.append(f"{output_directory}\{file}")
    return res


def parse_zevtc_logs_to_json(settings: UserSettings):
    exec_path = settings.get(EI_EXEC_PATH_KEY)
    input_path = settings.get(INPUT_DIRECTORY_KEY)
    output_path = settings.get(OUTPUT_DIRECTORY_KEY)
    if not exec_path or not input_path:
        missing_settings_warning_msg = (
            "Missing exec or input path, are your settings updated?"
        )
        logger.warn(missing_settings_warning_msg)
        raise Exception(missing_settings_warning_msg)
    output_path = output_path if output_path else input_path

    config_path = f"{os.getcwd()}\\gw2ei_config.conf".replace("\\", "/")
    files_array = get_logs_from_directory(input_path)
    logger.info(
        f"Attempting to parse {len(files_array)} logs from directory at {input_path} using executable at {exec_path}"
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
    logger.info("Parsing completed")
    return get_json_paths(output_directory=output_path)
