from typing import List
from pygw2agg.logic.support import sum_ressurects
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat

from pygw2agg.models.ei_output.log_data import LogData, to_individual_player_log_data


def get_player_account(player_name: str, log: LogData):
    return next(player.account for player in log.players if player.name == player_name)


def get_player_profession(player_name: str, log: LogData):
    return next(
        player.profession for player in log.players if player.name == player_name
    )


def get_player_totals_stats(player_name: str, logs: List[LogData]):
    pruned_logs = list(
        map(to_individual_player_log_data(player_name=player_name), logs)
    )
    return [sum_ressurects([log.player.support[0] for log in pruned_logs])]


def aggregate_player_logs(player_name: str, logs: List[LogData]):
    player_profession = get_player_profession(player_name=player_name, log=logs[0])
    player_account = get_player_account(player_name=player_name, log=logs[0])

    player_total_stats: List[AggregatedPlayerStat] = get_player_totals_stats(
        player_name, logs
    )

    return AggregatedPlayer(
        name=player_name,
        account=player_account,
        profession=player_profession,
        stats=player_total_stats,
    )
