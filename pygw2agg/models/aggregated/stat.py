from typing import Generic, List, TypeVar
from pygw2agg.models.aggregated.base import BaseAggregatedModel

AggregateStatValue = TypeVar("AggregateStatValue")


class AggregatedPlayerStat(BaseAggregatedModel, Generic[AggregateStatValue]):
    key: str
    value: AggregateStatValue
    friendly_name: str
    tags: List[str]
