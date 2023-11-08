from decimal import Decimal
from typing import List
from pygw2agg.logic.utils import get_avg_stat_by_min, get_stat_by_key
from pygw2agg.models.aggregated.defense import (
    AvgDodgeCount,
    TotalDodgeCount,
    get_total_dodge_count_key,
)
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat

from pygw2agg.models.ei_output.player_defenses_stats import PlayerDefensesStats


def sum_dodges(player_defense_stats: List[PlayerDefensesStats]):
    return TotalDodgeCount(
        value=sum([stat.dodgeCount for stat in player_defense_stats]),
    )


def avg_dodges(player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]):
    return AvgDodgeCount(
        value=round(
            get_avg_stat_by_min(
                time_value=player_active_time,
                stat_value=get_stat_by_key(
                    key=get_total_dodge_count_key(), stats_list=totals_stats
                ).value,
            ),
            ndigits=2,
        )
    )
