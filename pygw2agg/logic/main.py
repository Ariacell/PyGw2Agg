from typing import List

import structlog
from pygw2agg.logic.player import aggregate_player_logs
from pygw2agg.logic.utils import flatten_list
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.ei_output.log_data import LogData

logger = structlog.get_logger("logic_main")


def get_squad_player_names(log: LogData):
    return [player.name for player in log.players if player.notInSquad == False]


def get_unique_players_for_log_set(log_dataset: List[LogData]):
    return set(flatten_list(list(map(get_squad_player_names, log_dataset))))


def safe_string_list_get(l, key):
    try:
        return l.index(key)
    except ValueError:
        return False


def get_logs_involving_player(player_name: str, log_dataset: List[LogData]):
    logs_to_return = []
    for log in log_dataset:
        playerData = [player for player in log.players if player_name == player.name]
        if playerData == [] or len(playerData) > 1:
            break
        safePlayerData = playerData[0]
        if safePlayerData.defenses[0].damageTaken != 0:
            print(f"This one would be added!")
            logs_to_return.append(log)
    print(f"Got {len(logs_to_return)} for {player_name}")
    return logs_to_return
    # return [
    #     log
    #     for log in log_dataset
    #     if any(
    #         player
    #         for player in log.players
    #         if (
    #             # get_squad_player_names(log=log).index(player_name) != -1
    #             player.defenses[0].damageTaken
    #             != 0
    #         )
    #     )
    # ]


def get_logs_lists_per_player(
    player_names: List[str], log_dataset: List[LogData]
) -> List[List[LogData]]:
    res = {}
    for player_name in player_names:
        logs_for_player = get_logs_involving_player(
            player_name=player_name, log_dataset=log_dataset
        )
        res[player_name] = logs_for_player
    return res


def aggregate_log_data(log_dataset: List[LogData]) -> List[AggregatedPlayer]:
    logger.info(f"Aggregating {len(log_dataset)} logs")
    deuped_player_names = get_unique_players_for_log_set(log_dataset=log_dataset)
    log_lists = get_logs_lists_per_player(
        player_names=deuped_player_names, log_dataset=log_dataset
    )
    aggregate_player_data = []
    for player_name, logs_containing_player in log_lists.items():
        logger.debug(
            f"Found {len(logs_containing_player)} logs for player {player_name}"
        )
        aggregate_player_data.append(
            aggregate_player_logs(player_name, logs_containing_player)
        )
    return aggregate_player_data
