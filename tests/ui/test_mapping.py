from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.common.professions import ProfessionEnum
from pygw2agg.ui.mapping import map_aggregated_data_to_table_structure


def test_should_map_any_fields_present_in_data_to_appropriate_index_for_heading_in_table():
    test_summary_headings = [
        "empty",
        "another empty",
        "Populate Me",
        "more empty",
        "I Should Have Data",
    ]

    test_defense_headings = [
        "empty",
        "another empty",
        "heading isnt same as summary",
        "more empty",
        "I Should Have Data",
    ]

    player_stats_1 = AggregatedPlayerStat(
        friendly_name="Populate Me", key="populate_me", tags=["some tag"], value=30
    )
    player_stats_2 = AggregatedPlayerStat(
        friendly_name="I Should Have Data", key="have_data", tags=["some tag"], value=20
    )

    player_data = AggregatedPlayer(
        name="anything",
        account="anythingelse",
        profession=ProfessionEnum.berserker.value,
        stats=[player_stats_1, player_stats_2],
    )

    table_data = map_aggregated_data_to_table_structure(
        summary_headings=test_summary_headings,
        defense_headings=test_defense_headings,
        aggregated_data=[player_data],
    )

    assert table_data.summary == [
        [
            player_data.name,
            player_data.account,
            player_data.profession,
            None,
            None,
            30,
            None,
            20,
        ]
    ]
    assert table_data.defense == [
        [
            player_data.name,
            player_data.account,
            player_data.profession,
            None,
            None,
            None,
            None,
            20,
        ]
    ]
