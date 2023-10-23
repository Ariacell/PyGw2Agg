from decimal import Decimal, Context
from typing import List
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat


def sum(a, b):
    return a + b


def flatten_list(list):
    return [item for sublist in list for item in sublist]


def get_stat_by_key(key: str, stats_list: List[AggregatedPlayerStat]):
    return next(stat for stat in stats_list if stat.key == key)


def get_avg_stat_by_min(stat_value: Decimal | int, time_value: Decimal):
    return round(Decimal(stat_value / (time_value / 1000) * 60), 2)
