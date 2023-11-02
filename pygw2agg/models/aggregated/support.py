from decimal import Decimal
from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def get_total_cleanses_key():
    return "total_cleanses"


def get_total_cleanses_friendly_name():
    return "Total Cleanses"


class TotalCleanses(AggregatedPlayerStat):
    key: str = get_total_cleanses_key()
    friendly_name: str = get_total_cleanses_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.support.value]
    value: int


def get_average_cleanses_key():
    return "average_cleanses"


def get_average_cleanses_friendly_name():
    return "Average Cleanses"


class AvgCleanses(AggregatedPlayerStat):
    key: str = get_average_cleanses_key()
    friendly_name: str = get_average_cleanses_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.support.value]
    value: Decimal


class TotalSelfCleanses(AggregatedPlayerStat):
    key: str = "total_self_cleanses"
    friendly_name: str = ""
    tags: List[str] = [STAT_TAGS_ENUM.support.value]
    value: int


def get_total_resurrects_key():
    return "total_resurrects"


def get_total_resurrects_friendly_name():
    return "Resurrects"


class TotalResurrects(AggregatedPlayerStat):
    key: str = get_total_resurrects_key()
    friendly_name: str = get_total_resurrects_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.summary.value, STAT_TAGS_ENUM.support.value]
    value: int


def get_total_resurrect_time_key():
    return "total_resurrect_time"


def get_total_resurrect_time_friendly_name():
    return "Resurrect Time"


class TotalResurrectTime(AggregatedPlayerStat):
    key: str = get_total_resurrect_time_key()
    friendly_name: str = get_total_resurrect_time_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.summary.value, STAT_TAGS_ENUM.support.value]
    value: Decimal


def get_average_resurrects_key():
    return "average_resurrects"


def get_average_resurrects_friendly_name():
    return "Average Resurrects"


class AvgResurrects(AggregatedPlayerStat):
    key: str = get_average_resurrects_key()
    friendly_name: str = get_average_resurrects_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.support.value]
    value: Decimal


def get_average_resurrect_time_key():
    return "average_resurrect_time"


def get_average_resurrect_time_friendly_name():
    return "Average Resurrect Time"


class AvgResurrectTime(AggregatedPlayerStat):
    key: str = get_average_resurrect_time_key()
    friendly_name: str = get_average_resurrect_time_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.support.value]
    value: Decimal
