from typing import List
from pygw2agg.models.aggregated.player import AggregatedPlayer

from pygw2agg.models.ei_output.log_data import LogData


def get_player_account(player_name: str, log: LogData):
    return next(player.account for player in log.players if player.name == player_name)


def get_player_profession(player_name: str, log: LogData):
    return next(
        player.profession for player in log.players if player.name == player_name
    )


def aggregate_player_logs(player_name: str, logs: List[LogData]):
    player_profession = get_player_profession(player_name=player_name, log=logs[0])
    player_account = get_player_account(player_name=player_name, log=logs[0])

    return AggregatedPlayer(
        name=player_name,
        account=player_account,
        profession=player_profession,
        stats=[],
    )
