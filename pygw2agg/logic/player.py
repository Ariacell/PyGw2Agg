from datetime import timedelta
from decimal import Decimal
from functools import reduce
from typing import List
import structlog
from pygw2agg.logic.defense import (
    avg_deaths,
    avg_dmg_taken,
    avg_dodges,
    avg_times_downed,
    sum_deaths,
    sum_dmg_taken,
    sum_dodges,
    sum_times_downed,
)
from pygw2agg.logic.offense import (
    avg_downed_contribution,
    avg_dps,
    sum_damage,
    sum_down_contribution,
)
from pygw2agg.logic.support import (
    avg_cleanses,
    avg_resurrect_time,
    avg_resurrects,
    sum_cleanses,
    sum_ressurect_time,
    sum_ressurects,
)
from pygw2agg.logic.utility import (
    avg_distance_to_comm,
    avg_distance_to_squad,
    avg_interrupts,
    avg_strips,
    sum_interrupts,
    sum_rounds,
    sum_strips,
)
from pygw2agg.models.aggregated.misc import TotalActiveTime
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.domain.individual_player_log import IndividualPlayerLogData

from pygw2agg.models.ei_output.log_data import LogData, to_individual_player_log_data

logger = structlog.get_logger("logic_main")


def get_player_account(player_name: str, log: IndividualPlayerLogData):
    return log.player.account


def get_player_profession(player_name: str, log: IndividualPlayerLogData):
    return log.player.profession


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
    player_damage_logs = [log.player.dpsAll[0] for log in logs]
    player_misc_logs = [log.player.statsAll[0] for log in logs]
    player_defense_logs = [log.player.defenses[0] for log in logs]
    return [
        TotalActiveTime(
            value=get_player_human_friendly_active_time(
                get_player_total_active_time(logs=logs)
            )
        ),
        sum_ressurects(player_support_stats=player_support_logs),
        sum_cleanses(player_support_stats=player_support_logs),
        sum_ressurect_time(player_support_stats=player_support_logs),
        sum_strips(player_support_stats=player_support_logs),
        sum_interrupts(player_misc_logs=player_misc_logs),
        sum_damage(player_dps_all_stats=player_damage_logs),
        sum_dmg_taken(player_defense_stats=player_defense_logs),
        sum_down_contribution(player_all_stats=player_misc_logs),
        sum_times_downed(player_defense_stats=player_defense_logs),
        sum_deaths(player_defense_stats=player_defense_logs),
        sum_rounds(player_stats=logs),
        sum_dodges(player_defense_stats=player_defense_logs),
        avg_distance_to_comm(player_misc_stats=player_misc_logs),
        avg_distance_to_squad(player_misc_stats=player_misc_logs),
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
        avg_dps(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_downed_contribution(
            player_active_time=total_active_time, totals_stats=totals_stats
        ),
        avg_times_downed(
            player_active_time=total_active_time, totals_stats=totals_stats
        ),
        avg_strips(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_interrupts(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_deaths(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_dmg_taken(player_active_time=total_active_time, totals_stats=totals_stats),
        avg_dodges(player_active_time=total_active_time, totals_stats=totals_stats),
    ]


def aggregate_player_logs(player_name: str, logs: List[LogData]):
    simplified_player_logs: List[IndividualPlayerLogData] = list(
        map(to_individual_player_log_data(player_name=player_name), logs)
    )
    logger.debug(
        f"Got {len(simplified_player_logs)} simplified Individual Log Data for player {player_name}"
    )
    player_account = get_player_account(
        player_name=player_name, log=simplified_player_logs[0]
    )
    player_profession = get_player_profession(
        player_name=player_name, log=simplified_player_logs[0]
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
