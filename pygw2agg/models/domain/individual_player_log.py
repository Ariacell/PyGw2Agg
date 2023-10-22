from pygw2agg.models.domain.base import BaseDomainModel
from pygw2agg.models.ei_output.player import Player


class IndividualPlayerLogData(BaseDomainModel):
    timeStart: str
    duration: str
    recordedBy: str
    player: Player
