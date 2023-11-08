from decimal import Decimal
from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def get_total_rounds_key():
    return "total_rounds"


def get_total_rounds_friendly_name():
    return "Total Rounds"


class TotalRounds(AggregatedPlayerStat):
    key: str = get_total_rounds_key()
    friendly_name: str = get_total_rounds_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.utility.value]
    value: int


def get_avg_comm_distance_key():
    return "avg_comm_distance"


def get_avg_comm_distance_friendly_name():
    return "Avg Comm Dist"


class AvgCommDist(AggregatedPlayerStat):
    key: str = get_avg_comm_distance_key()
    friendly_name: str = get_avg_comm_distance_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.utility.value]
    value: int


def get_avg_squad_distance_key():
    return "avg_squad_distance"


def get_avg_squad_distance_friendly_name():
    return "Avg Squad Dist"


class AvgSquadDist(AggregatedPlayerStat):
    key: str = get_avg_squad_distance_key()
    friendly_name: str = get_avg_squad_distance_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.utility.value]
    value: int


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
