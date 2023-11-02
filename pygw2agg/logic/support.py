from decimal import Decimal
from functools import reduce
from typing import List
from pygw2agg.logic.utils import get_avg_stat_by_min, get_stat_by_key
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.aggregated.support import (
    AvgResurrectTime,
    AvgResurrects,
    TotalCleanses,
    TotalResurrectTime,
    get_total_cleanses_key,
    get_total_resurrect_time_key,
    get_total_resurrects_key,
    AvgCleanses,
    TotalResurrects,
)

from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_ressurects(player_support_stats: List[PlayerSupportStats]):
    return TotalResurrects(
        value=sum([stat.resurrects for stat in player_support_stats]),
    )


def sum_ressurect_time(player_support_stats: List[PlayerSupportStats]):
    return TotalResurrectTime(
        value=sum([stat.resurrectTime for stat in player_support_stats]),
    )


def sum_cleanses(player_support_stats: List[PlayerSupportStats]):
    return TotalCleanses(
        value=sum([stat.condiCleanse for stat in player_support_stats]),
    )


def avg_cleanses(player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]):
    return AvgCleanses(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_cleanses_key(), stats_list=totals_stats
            ).value,
        )
    )


def avg_resurrects(
    player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return AvgResurrects(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_resurrects_key(), stats_list=totals_stats
            ).value,
        )
    )


def avg_resurrect_time(
    player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return AvgResurrectTime(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_resurrect_time_key(), stats_list=totals_stats
            ).value,
        )
    )
