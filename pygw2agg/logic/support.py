from functools import reduce
from typing import List

from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_ressurects(player_support_stats: List[PlayerSupportStats]):
    reduce(
        sum,
        [
            player_support_stat.resurrects
            for player_support_stat in player_support_stats
        ],
        0,
    )
    pass
