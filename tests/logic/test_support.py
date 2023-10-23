from pygw2agg.logic.support import sum_cleanses, sum_ressurects
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.domain.individual_player_log import get_stub_individual_player_log
from pygw2agg.models.ei_output.player import get_stub_player
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
    assert res.value == 18


def test_sum_cleanses_should_return_total_cleanses_in_model_structure():
    support_logs = [
        get_stub_player_support_stats(condiCleanse=5),
        get_stub_player_support_stats(condiCleanse=6),
        get_stub_player_support_stats(condiCleanse=8),
    ]

    res = sum_cleanses(support_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Cleanses"
    assert res.key == "total_cleanses"
    assert res.tags == ["summary, support"]
    assert res.value == 19


def test_average_cleanses_should_return_cleanses_per_min():
    test_player_name = "PlayerName"
    test_total_stats = [AggregatedPlayerStat(friendly_name=)]
