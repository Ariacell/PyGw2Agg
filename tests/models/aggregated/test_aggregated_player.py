from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.common.professions import ProfessionEnum


def test_get_stat_by_key_should_return_the_stat_object_with_associated_key():
    key_to_find = "this_one"
    test_stat_1 = AggregatedPlayerStat(
        value=424.34,
        friendly_name="First Value",
        key="not_this_one",
        tags=["some", "tags"],
    )
    test_stat_2 = AggregatedPlayerStat(
        value="Found me!",
        friendly_name="Next Value",
        key=key_to_find,
        tags=["some", "tags"],
    )
    test_stat_3 = AggregatedPlayerStat(
        value=42,
        friendly_name="Final Value",
        key="not_this_one_either",
        tags=["some", "tags"],
    )
    test_agg_player = AggregatedPlayer(
        name="anything",
        account="anythine.1234",
        profession=ProfessionEnum.catalyst.value,
        stats=[test_stat_1, test_stat_2, test_stat_3],
    )

    assert test_agg_player.get_stat_by_key(key_to_find) == test_stat_2
