from decimal import Decimal
from functools import reduce
from typing import List
from pygw2agg.logic.support import sum_cleanses, sum_ressurects
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.domain.individual_player_log import IndividualPlayerLogData

from pygw2agg.models.ei_output.log_data import LogData, to_individual_player_log_data


def get_player_account(player_name: str, log: LogData):
    return next(player.account for player in log.players if player.name == player_name)


def get_player_profession(player_name: str, log: LogData):
    return next(
        player.profession for player in log.players if player.name == player_name
    )


#  Active time is returned in milliseconds for flexibility in calculations
def get_player_total_active_time(logs: List[IndividualPlayerLogData]):
    logs_active_times = 0
    for log in logs:
        logs_active_times += sum(log.player.activeTimes)
    return logs_active_times


def get_player_total_active_rounds(logs: List[IndividualPlayerLogData]):
    return len(logs)


def get_player_totals_stats(player_name: str, logs: List[IndividualPlayerLogData]):
    player_support_logs = [log.player.support[0] for log in logs]
    return [sum_ressurects(player_support_logs), sum_cleanses(player_support_logs)]


def get_player_averages_stats(
    total_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
):
    return []


def aggregate_player_logs(player_name: str, logs: List[LogData]):
    player_profession = get_player_profession(player_name=player_name, log=logs[0])
    player_account = get_player_account(player_name=player_name, log=logs[0])
    simplified_player_logs = list(
        map(to_individual_player_log_data(player_name=player_name), logs)
    )
    player_total_stats: List[AggregatedPlayerStat] = get_player_totals_stats(
        player_name, simplified_player_logs
    )

    return AggregatedPlayer(
        name=player_name,
        account=player_account,
        profession=player_profession,
        stats=player_total_stats,
    )
