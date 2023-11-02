from decimal import Decimal
from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def get_total_strips_key():
    return "total_strips"


def get_total_strips_friendly_name():
    return "Total Strips"


class TotalStrips(AggregatedPlayerStat):
    key: str = get_total_strips_key()
    friendly_name: str = get_total_strips_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.utility.value]
    value: int


def get_average_strips_key():
    return "average_strips"


def get_average_strips_friendly_name():
    return "Average Strips"


class AvgStrips(AggregatedPlayerStat):
    key: str = get_average_strips_key()
    friendly_name: str = get_average_strips_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.utility.value]
    value: Decimal
