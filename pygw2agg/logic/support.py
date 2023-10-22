from functools import reduce
from typing import List
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat

from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


def sum_ressurects(player_support_stats: List[PlayerSupportStats]):
    return AggregatedPlayerStat(
        value=sum([stat.resurrects for stat in player_support_stats]),
        friendly_name="Ressurects",
        key="total_ressurects",
        tags=["summary, support"],
    )


def sum_cleanses(player_support_stats: List[PlayerSupportStats]):
    return AggregatedPlayerStat(
        value=sum([stat.condiCleanse for stat in player_support_stats]),
        friendly_name="Cleanses",
        key="total_cleanses",
        tags=["summary, support"],
    )


def sum_cleanses(player_support_stats: List[PlayerSupportStats]):
    return AggregatedPlayerStat(
        value=sum([stat.condiCleanse for stat in player_support_stats]),
        friendly_name="Cleanses",
        key="total_cleanses",
        tags=["summary, support"],
    )
