from decimal import Decimal
from typing import List
from pygw2agg.logic.utils import get_avg_stat_by_min, get_stat_by_key
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.aggregated.utility import (
    AvgCommDist,
    AvgInterrupts,
    AvgSquadDist,
    AvgStrips,
    TotalInterrupts,
    TotalRounds,
    TotalStrips,
    get_total_interrupts_key,
    get_total_strips_key,
)
from pygw2agg.models.domain.individual_player_log import IndividualPlayerLogData
from pygw2agg.models.ei_output.player_misc_stats import PlayerMiscStats
from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_strips(player_support_stats: List[PlayerSupportStats]):
    return TotalStrips(
        value=sum([stat.boonStrips for stat in player_support_stats]),
    )


def avg_strips(player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]):
    return AvgStrips(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_strips_key(), stats_list=totals_stats
            ).value,
        )
    )


def sum_interrupts(player_misc_logs: List[PlayerMiscStats]):
    return TotalInterrupts(
        value=sum([stat.interrupts for stat in player_misc_logs]),
    )


def avg_interrupts(
    player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return AvgInterrupts(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_interrupts_key(), stats_list=totals_stats
            ).value,
        )
    )


def sum_rounds(player_stats: List[IndividualPlayerLogData]):
    return TotalRounds(value=len(player_stats))


def avg_distance_to_comm(player_misc_stats: List[PlayerMiscStats]):
    return AvgCommDist(
        value=int(
            (
                sum([stat.distToCom for stat in player_misc_stats])
                / len(player_misc_stats)
            )
        ),
    )


def avg_distance_to_squad(player_misc_stats: List[PlayerMiscStats]):
    return AvgSquadDist(
        value=int(
            (
                sum([stat.stackDist for stat in player_misc_stats])
                / len(player_misc_stats)
            )
        ),
    )
