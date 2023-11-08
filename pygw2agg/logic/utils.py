from decimal import Decimal, Context
from functools import reduce
from typing import List

import structlog
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat

logger = structlog.get_logger("logic_utils")


def sum(a, b):
    return a + b


def flatten_list(list):
    return [item for sublist in list for item in sublist]


def get_stat_by_key(key: str, stats_list: List[AggregatedPlayerStat]):
    try:
        stat = next(stat for stat in stats_list if stat.key == key)
    except Exception as e:
        logger.error(f"Unable to find required stat '{key}' in aggregate stats list.")
        raise e
    return stat


def get_avg_stat_by_min(stat_value: Decimal | int, time_value: Decimal):
    return round(Decimal(stat_value / (time_value / Decimal(1000)) * 60), 2)


def get_avg_stat_by_sec(stat_value: Decimal | int, time_value: Decimal):
    return round(Decimal(stat_value / (time_value / Decimal(1000))), 2)
