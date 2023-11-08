from decimal import Decimal
from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def get_total_damage_key():
    return "total_damage"


def get_total_damage_friendly_name():
    return "Total Damage"


class TotalDamage(AggregatedPlayerStat):
    key: str = get_total_damage_key()
    friendly_name: str = get_total_damage_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.offense.value, STAT_TAGS_ENUM.summary.value]
    value: Decimal


def get_average_dps_key():
    return "average_dps"


def get_average_dps_friendly_name():
    return "Average Dps"


class AvgDps(AggregatedPlayerStat):
    key: str = get_average_dps_key()
    friendly_name: str = get_average_dps_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.offense.value]
    value: Decimal


def get_total_downed_contribution_key():
    return "total_down_contribution"


def get_total_downed_contribution_friendly_name():
    return "Total Down Contribution"


class TotalDownContribution(AggregatedPlayerStat):
    key: str = get_total_downed_contribution_key()
    friendly_name: str = get_total_downed_contribution_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.offense.value, STAT_TAGS_ENUM.summary.value]
    value: Decimal


def get_average_downed_contribution_key():
    return "average_downed_contribution"


def get_average_downed_contribution_friendly_name():
    return "Average Down Contribution"


class AvgDownedContribution(AggregatedPlayerStat):
    key: str = get_average_downed_contribution_key()
    friendly_name: str = get_average_downed_contribution_friendly_name()
    tags: List[str] = [STAT_TAGS_ENUM.offense.value]
    value: Decimal
