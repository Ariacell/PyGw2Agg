from typing import Any, List
from pygw2agg.models.domain.base import BaseDomainModel


class TableModel(BaseDomainModel):
    summary: List[Any]
    defense: List[Any]
    offense: List[Any]
    utility: List[Any]
