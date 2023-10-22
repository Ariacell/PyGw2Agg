from pygw2agg.models.domain.base import BaseDomainModel
from pygw2agg.models.ei_output.player import Player, get_stub_player


class IndividualPlayerLogData(BaseDomainModel):
    timeStart: str
    duration: str
    recordedBy: str
    player: Player


def get_stub_individual_player_log(
    duration="00m 33s 966ms",
    player=get_stub_player(),
    recorded_by="someone",
    time_start="2023-05-14 21:54:45 +10",
):
    return IndividualPlayerLogData(
        duration=duration, player=player, recordedBy=recorded_by, timeStart=time_start
    )
