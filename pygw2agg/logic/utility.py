from typing import List
from pygw2agg.models.aggregated.utility import TotalStrips
from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_strips(player_support_stats: List[PlayerSupportStats]):
    return TotalStrips(
        value=sum([stat.boonStrips for stat in player_support_stats]),
    )
