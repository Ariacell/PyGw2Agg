from typing import List
from pygw2agg.models.aggregated.base import BaseAggregatedModel
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.common.professions import ProfessionEnum


class AggregatedPlayer(BaseAggregatedModel):
    name: str
    account: str
    profession: ProfessionEnum
    stats: List[AggregatedPlayerStat]
