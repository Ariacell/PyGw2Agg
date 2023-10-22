from typing import List
from pygw2agg.models.aggregated.base import BaseAggregatedModel
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.common.professions import ProfessionEnum


class AggregatedPlayer(BaseAggregatedModel):
    name: str
    account: str
    profession: ProfessionEnum
    stats: List[AggregatedPlayerStat]

    def get_stat_by_key(
        self,
        key: str,
    ):
        return next(stat for stat in self.stats if stat.key == key)
