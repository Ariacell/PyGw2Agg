from typing import List
from pygw2agg.models.aggregated.offense import TotalDamage, TotalDownContribution
from pygw2agg.models.ei_output.player_dps_all_stats import PlayerDpsAllStats
from pygw2agg.models.ei_output.player_misc_stats import PlayerMiscStats
from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_damage(player_dps_all_stats: List[PlayerDpsAllStats]):
    return TotalDamage(
        value=sum([stat.damage for stat in player_dps_all_stats]),
    )


def sum_down_contribution(player_all_stats: List[PlayerMiscStats]):
    return TotalDownContribution(
        value=sum([stat.downContribution for stat in player_all_stats]),
    )
