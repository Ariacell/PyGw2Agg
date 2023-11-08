from decimal import Decimal
from typing import List
from pygw2agg.logic.utils import (
    get_avg_stat_by_min,
    get_avg_stat_by_sec,
    get_stat_by_key,
)
from pygw2agg.models.aggregated.offense import (
    AvgDownedContribution,
    AvgDps,
    TotalDamage,
    TotalDownContribution,
    get_total_damage_key,
    get_total_downed_contribution_key,
)
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.ei_output.player_dps_all_stats import PlayerDpsAllStats
from pygw2agg.models.ei_output.player_misc_stats import PlayerMiscStats
from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_damage(player_dps_all_stats: List[PlayerDpsAllStats]):
    return TotalDamage(
        value=sum([stat.damage for stat in player_dps_all_stats]),
    )


def avg_dps(player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]):
    return AvgDps(
        value=get_avg_stat_by_sec(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_damage_key(), stats_list=totals_stats
            ).value,
        )
    )


def sum_down_contribution(player_all_stats: List[PlayerMiscStats]):
    return TotalDownContribution(
        value=sum([stat.downContribution for stat in player_all_stats]),
    )


def avg_downed_contribution(
    player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return AvgDownedContribution(
        value=get_avg_stat_by_min(
            time_value=player_active_time,
            stat_value=get_stat_by_key(
                key=get_total_downed_contribution_key(), stats_list=totals_stats
            ).value,
        )
    )
