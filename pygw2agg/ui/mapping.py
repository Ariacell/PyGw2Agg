from typing import List
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.ui.table import (
    AGGREGATE_TABLE_DEFENSE_HEADINGS,
    AGGREGATE_TABLE_SUMMARY_HEADINGS,
)
from pygw2agg.ui.table_model import TableModel


def get_headings_values(headings: List[str], player_data: AggregatedPlayer):
    heading_values = [None] * len(headings)
    stats_list = player_data.stats
    for i, heading in enumerate(headings):
        for stat in stats_list:
            if stat.friendly_name == heading:
                heading_values[i] = stat.value
    return heading_values


def map_aggregated_data_to_table_structure(
    aggregated_data: List[AggregatedPlayer],
    summary_headings: List[str] = AGGREGATE_TABLE_SUMMARY_HEADINGS,
    defense_headings: List[str] = AGGREGATE_TABLE_DEFENSE_HEADINGS,
) -> TableModel:
    total_summary_table_data = []
    total_defense_table_data = []
    for player in aggregated_data:
        base_data = [player.name, player.account, player.profession.value]
        total_summary_table_data.append(
            base_data + get_headings_values(summary_headings, player)
        )
        total_defense_table_data.append(
            base_data + get_headings_values(defense_headings, player)
        )
    return TableModel(
        summary=total_summary_table_data,
        defense=total_defense_table_data,
    )
