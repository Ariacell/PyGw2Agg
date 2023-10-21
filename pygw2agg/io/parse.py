import os
import subprocess
import structlog


logger = structlog.get_logger("io_parsing")


def get_logs_from_directory(input_directory):
    res = []
    # Iterate directory
    for file in os.listdir(input_directory):
        # check only text files
        if file.endswith(".zevtc"):
            res.append(f"{input_directory}\{file}")
    return res


def parse_zevtc_logs_to_json(exec_path: str, input_path: str, output_path: str | None):
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
