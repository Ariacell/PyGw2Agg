from decimal import Decimal
from typing import List
from pygw2agg.logic.utils import (
    get_avg_stat_by_min,
    get_avg_stat_by_sec,
    get_stat_by_key,
)
from pygw2agg.models.aggregated.defense import (
    AvgDamageTaken,
    AvgDeaths,
    AvgDodgeCount,
    AvgTimesDowned,
    TotalDamageTaken,
    TotalDeaths,
    TotalDodgeCount,
    TotalTimesDowned,
    get_total_damage_taken_key,
    get_total_deaths_key,
    get_total_dodge_count_key,
    get_total_times_downed_key,
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


def sum_dmg_taken(player_defense_stats: List[PlayerDefensesStats]):
    return TotalDamageTaken(
        value=sum([stat.damageTaken for stat in player_defense_stats]),
    )


def avg_dmg_taken(
    player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return AvgDamageTaken(
        value=round(
            get_avg_stat_by_sec(
                time_value=player_active_time,
                stat_value=get_stat_by_key(
                    key=get_total_damage_taken_key(), stats_list=totals_stats
                ).value,
            ),
            ndigits=2,
        )
    )


def sum_times_downed(player_defense_stats: List[PlayerDefensesStats]):
    return TotalTimesDowned(
        value=sum([stat.downCount for stat in player_defense_stats]),
    )


def avg_times_downed(
    player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return AvgTimesDowned(
        value=round(
            get_avg_stat_by_min(
                time_value=player_active_time,
                stat_value=get_stat_by_key(
                    key=get_total_times_downed_key(), stats_list=totals_stats
                ).value,
            ),
            ndigits=2,
        )
    )


def sum_deaths(player_defense_stats: List[PlayerDefensesStats]):
    return TotalDeaths(
        value=sum([stat.deadCount for stat in player_defense_stats]),
    )


def avg_deaths(player_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]):
    return AvgDeaths(
        value=round(
            get_avg_stat_by_min(
                time_value=player_active_time,
                stat_value=get_stat_by_key(
                    key=get_total_deaths_key(), stats_list=totals_stats
                ).value,
            ),
            ndigits=2,
        )
    )
