from pygw2agg.logic.utility import sum_strips
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.ei_output.player_support_stats import get_stub_player_support_stats


def test_sum_strips_should_return_total_strips_in_model_structure():
    support_logs = [
        get_stub_player_support_stats(boonStrips=5),
        get_stub_player_support_stats(boonStrips=6),
        get_stub_player_support_stats(boonStrips=7),
    ]

    res = sum_strips(support_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Total Strips"
    assert res.key == "total_strips"
    assert res.tags == ["utility"]
    assert res.value == 18
