from pygw2agg.logic.support import (
    avg_cleanses,
    avg_resurrect_time,
    avg_resurrects,
    sum_cleanses,
    sum_ressurect_time,
    sum_ressurects,
)
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.domain.individual_player_log import get_stub_individual_player_log
from pygw2agg.models.ei_output.player import get_stub_player
from pygw2agg.models.ei_output.player_support_stats import get_stub_player_support_stats
from pygw2agg.models.aggregated.support import (
    AvgResurrectTime,
    AvgResurrects,
    TotalCleanses,
    TotalResurrectTime,
    AvgCleanses,
    TotalResurrects,
)


def test_sum_ressurects_should_return_total_resurrects_in_model_structure():
    support_logs = [
        get_stub_player_support_stats(resurrects=5),
        get_stub_player_support_stats(resurrects=6),
        get_stub_player_support_stats(resurrects=7),
    ]

    res = sum_ressurects(support_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Resurrects"
    assert res.key == "total_resurrects"
    assert res.tags == ["summary", "support"]
    assert res.value == 18


def test_sum_cleanses_should_return_total_cleanses_in_model_structure():
    support_logs = [
        get_stub_player_support_stats(condiCleanse=5),
        get_stub_player_support_stats(condiCleanse=6),
        get_stub_player_support_stats(condiCleanse=8),
    ]

    res = sum_cleanses(support_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Total Cleanses"
    assert res.key == "total_cleanses"
    assert res.tags == ["support"]
    assert res.value == 19


def test_total_resurrect_time_should_return_total_time_spent_resurrecting_in_model_structure():
    support_logs = [
        get_stub_player_support_stats(resurrectTime=10.0),
        get_stub_player_support_stats(resurrectTime=40.0),
        get_stub_player_support_stats(resurrectTime=20.0),
    ]

    res = sum_ressurect_time(support_logs)

    assert res == TotalResurrectTime(value=70.0)


def test_average_cleanses_should_return_cleanses_per_min():
    test_total_stats = [TotalCleanses(value=24)]
    test_player_playtime = 60000  # 1 minute in ms
    assert avg_cleanses(
        player_active_time=test_player_playtime, totals_stats=test_total_stats
    ) == AvgCleanses(value=24)


def test_average_resurrects_should_return_resurrects_per_min():
    test_total_stats = [TotalResurrects(value=54)]
    test_player_playtime = 30000  # 30s in ms
    assert avg_resurrects(
        player_active_time=test_player_playtime, totals_stats=test_total_stats
    ) == AvgResurrects(value=(54 * 2))


def test_average_resurrect_time_should_return_resurrect_time_per_min():
    test_total_stats = [TotalResurrectTime(value=54.0)]
    test_player_playtime = 30000  # 30s in ms
    assert avg_resurrect_time(
        player_active_time=test_player_playtime, totals_stats=test_total_stats
    ) == AvgResurrectTime(value=(54 * 2))
