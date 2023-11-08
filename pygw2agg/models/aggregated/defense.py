from decimal import Decimal
from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def get_total_dodge_count_key():
    return "total_dodge_count"


def get_total_dodge_count_friendly_name():
    return "Total Dodges"


class TotalDodgeCount(AggregatedPlayerStat):
    key: str = get_total_dodge_count_key()
    friendly_name: str = get_total_dodge_count_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: int


def get_avg_dodge_count_key():
    return "avg_dodge_count"


def get_avg_dodge_count_friendly_name():
    return "Avg Dodges"


class AvgDodgeCount(AggregatedPlayerStat):
    key: str = get_avg_dodge_count_key()
    friendly_name: str = get_avg_dodge_count_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: Decimal
