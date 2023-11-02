from typing import List
from pygw2agg.models.aggregated.base import STAT_TAGS_ENUM
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat

active_time_key = "total_self_cleanses"
active_time_friendly_name = "Active Time"


class TotalActiveTime(AggregatedPlayerStat):
    key: str = active_time_key
    friendly_name: str = active_time_friendly_name
    tags: List[str] = [STAT_TAGS_ENUM.common.value]
    value: str
