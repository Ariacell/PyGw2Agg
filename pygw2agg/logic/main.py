from typing import List

import structlog
from pygw2agg.logic.utils import flatten_list
from pygw2agg.models.ei_output.log_data import LogData

logger = structlog.get_logger("logic_main")


def get_player_names(log: LogData):
    return [player.name for player in log.players]


def aggregate_log_data(log_data: List[LogData]):
    logger.info(f"Aggregating {len(log_data)} logs")
    players = set(flatten_list(list(map(get_player_names, log_data))))
    return players
