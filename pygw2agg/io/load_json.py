import json
import os
import pydantic

import structlog

from pygw2agg.models.ei_output.log_data import LogData

logger = structlog.get_logger("io_loading_json")


def load_json(json_paths: [str]):
    type_adapter = pydantic.TypeAdapter(LogData)
    modelled_data = []
    for filepath in json_paths:
        file = open(file=filepath)
        json_data = json.load(file)
        data = type_adapter.validate_python(json_data)
        logger.info(
            f"Loaded log starting at {data.timeStart} with duration {data.duration}"
        )
        modelled_data.append(data)
        file.close()
    return modelled_data
