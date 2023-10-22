from typing import List
from pydantic import BaseModel
from pygw2agg.models.domain.individual_player_log import IndividualPlayerLogData
from pygw2agg.models.ei_output.base_ei_model import BaseEiJsonModel

from pygw2agg.models.ei_output.player import Player, get_stub_player_stats


class LogData(BaseEiJsonModel):
    timeStart: str
    duration: str
    recordedBy: str
    players: List[Player]


def to_individual_player_log_data(player_name: str):
    def map_to_individual_logs(log: LogData):
        return IndividualPlayerLogData(
            timeStart=log.timeStart,
            duration=log.duration,
            recordedBy=log.recordedBy,
            player=next(player for player in log.players if player.name == player_name),
        )

    return map_to_individual_logs


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
