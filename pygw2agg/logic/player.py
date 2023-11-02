from datetime import timedelta
from decimal import Decimal
from functools import reduce
from typing import List
from pygw2agg.logic.support import (
    avg_cleanses,
    avg_resurrect_time,
    avg_resurrects,
    sum_cleanses,
    sum_ressurect_time,
    sum_ressurects,
)
from pygw2agg.models.aggregated.misc import TotalActiveTime
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


def get_player_human_friendly_active_time(active_time: Decimal):
    time_parts = str(timedelta(milliseconds=int(active_time))).split(".")
    return time_parts[0] + "." + time_parts[1][:3] + "ms"


def get_player_total_active_rounds(logs: List[IndividualPlayerLogData]):
    return len(logs)


def get_player_totals_stats(player_name: str, logs: List[IndividualPlayerLogData]):
    player_support_logs = [log.player.support[0] for log in logs]
    return [
        TotalActiveTime(
            value=get_player_human_friendly_active_time(
                get_player_total_active_time(logs=logs)
            )
        ),
        sum_ressurects(player_support_stats=player_support_logs),
        sum_cleanses(player_support_stats=player_support_logs),
        sum_ressurect_time(player_support_stats=player_support_logs),
    ]


def get_player_averages_stats(
    total_active_time: Decimal, totals_stats: List[AggregatedPlayerStat]
) -> List[AggregatedPlayerStat]:
    return [
        avg_cleanses(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_resurrects(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_resurrect_time(
            player_active_time=total_active_time, totals_stats=totals_stats
        ),
    ]


def aggregate_player_logs(player_name: str, logs: List[LogData]):
    player_profession = get_player_profession(player_name=player_name, log=logs[0])
    player_account = get_player_account(player_name=player_name, log=logs[0])
    simplified_player_logs: List[IndividualPlayerLogData] = list(
        map(to_individual_player_log_data(player_name=player_name), logs)
    )
    player_totals_stats: List[AggregatedPlayerStat] = get_player_totals_stats(
        player_name, simplified_player_logs
    )
    player_avg_stats = get_player_averages_stats(
        get_player_total_active_time(logs=simplified_player_logs),
        totals_stats=player_totals_stats,
    )

    return AggregatedPlayer(
        name=player_name,
        account=player_account,
        profession=player_profession,
        stats=player_totals_stats + player_avg_stats,
    )
