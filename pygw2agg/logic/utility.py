from typing import List
from pygw2agg.models.aggregated.utility import (
    AvgCommDist,
    AvgSquadDist,
    TotalRounds,
    TotalStrips,
)
from pygw2agg.models.domain.individual_player_log import IndividualPlayerLogData
from pygw2agg.models.ei_output.player_misc_stats import PlayerMiscStats
from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_strips(player_support_stats: List[PlayerSupportStats]):
    return TotalStrips(
        value=sum([stat.boonStrips for stat in player_support_stats]),
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
