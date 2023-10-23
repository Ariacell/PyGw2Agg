from decimal import Decimal
from functools import reduce
from typing import List
from pygw2agg.logic.utils import get_avg_stat_by_min, get_stat_by_key
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.aggregated.support import (
    total_cleanses_key,
    AvgCleanses,
    TotalRessurects,
)

from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_ressurects(player_support_stats: List[PlayerSupportStats]):
    return TotalRessurects(
        value=sum([stat.resurrects for stat in player_support_stats]),
    )


def sum_cleanses(player_support_stats: List[PlayerSupportStats]):
    return AggregatedPlayerStat(
        value=sum([stat.condiCleanse for stat in player_support_stats]),
        friendly_name="Cleanses",
        key="total_cleanses",
        tags=["summary, support"],
    )


def avg_cleanses(player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]):
    return AvgCleanses(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=total_cleanses_key, stats_list=totals_stats
            ).value,
        )
    )
