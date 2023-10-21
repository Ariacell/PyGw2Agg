from typing import List
from pydantic import BaseModel
from pygw2agg.models.ei_output.base_ei_model import BaseEiJsonModel

from pygw2agg.models.ei_output.player import Player


class LogData(BaseEiJsonModel):
    timeStart: str
    duration: str
    recordedBy: str
    players: List[Player]
