from typing import List
from pydantic import BaseModel
from pygw2agg.models.ei_output.base_ei_model import BaseEiJsonModel

from pygw2agg.models.ei_output.player import Player, get_stub_player_stats


class LogData(BaseEiJsonModel):
    timeStart: str
    duration: str
    recordedBy: str
    players: List[Player]


def get_stub_log(
    duration="sometime",
    recordedBy="someone",
    timeStart="yesterday",
    players=[get_stub_player_stats()],
):
    return LogData(
        duration=duration,
        recordedBy=recordedBy,
        timeStart=timeStart,
        players=players,
    )
