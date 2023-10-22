from pygw2agg.logic.support import sum_ressurects
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.ei_output.player_support_stats import get_stub_player_support_stats


def test_sum_ressurects_should_return_total_resurrects_in_model_structure():
    support_logs = [
        get_stub_player_support_stats(resurrects=5),
        get_stub_player_support_stats(resurrects=6),
        get_stub_player_support_stats(resurrects=7),
    ]

    res = sum_ressurects(support_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Ressurects"
    assert res.key == "total_ressurects"
    assert res.tags == ["summary, support"]
