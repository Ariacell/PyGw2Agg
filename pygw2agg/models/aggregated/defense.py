from decimal import Decimal
from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def get_total_damage_taken_key():
    return "total_damage_taken"


def get_total_damage_taken_friendly_name():
    return "Total Damage Taken"


class TotalDamageTaken(AggregatedPlayerStat):
    key: str = get_total_damage_taken_key()
    friendly_name: str = get_total_damage_taken_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: int


def get_avg_damage_taken_key():
    return "avg_damage_taken"


def get_avg_damage_taken_friendly_name():
    return "Avg Dps Taken"


class AvgDamageTaken(AggregatedPlayerStat):
    key: str = get_avg_damage_taken_key()
    friendly_name: str = get_avg_damage_taken_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: Decimal


def get_total_times_downed_key():
    return "total_times_downed"


def get_total_times_downed_friendly_name():
    return "Times Downed"


class TotalTimesDowned(AggregatedPlayerStat):
    key: str = get_total_times_downed_key()
    friendly_name: str = get_total_times_downed_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: int


def get_avg_downs_per_min_key():
    return "avg_downs_per_min"


def get_avg_downs_per_min_friendly_name():
    return "Avg Times Downed"


class AvgTimesDowned(AggregatedPlayerStat):
    key: str = get_avg_downs_per_min_key()
    friendly_name: str = get_avg_downs_per_min_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: Decimal


# DEATHS


def get_total_deaths_key():
    return "total_deaths"


def get_total_deaths_friendly_name():
    return "Total Deaths"


class TotalDeaths(AggregatedPlayerStat):
    key: str = get_total_deaths_key()
    friendly_name: str = get_total_deaths_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: int


def get_avg_deaths_per_min_key():
    return "avg_deaths_per_min"


def get_avg_deaths_per_min_friendly_name():
    return "Avg Deaths"


class AvgDeaths(AggregatedPlayerStat):
    key: str = get_avg_deaths_per_min_key()
    friendly_name: str = get_avg_deaths_per_min_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.defense.value]
    value: Decimal


# /DEATHS

# DODGES


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


# /DODGES
