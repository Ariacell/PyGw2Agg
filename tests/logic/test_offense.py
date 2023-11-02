from pygw2agg.logic.offense import sum_damage, sum_down_contribution
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.ei_output.player_dps_all_stats import get_stub_player_dps_all_stats
from pygw2agg.models.ei_output.player_misc_stats import get_stub_player_misc_stats


def test_sum_damage_should_return_total_outgoing_damage_in_model_structure():
    dps_all_logs = [
        get_stub_player_dps_all_stats(damage=24.5),
        get_stub_player_dps_all_stats(damage=25.50),
        get_stub_player_dps_all_stats(damage=50),
    ]

    res = sum_damage(dps_all_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Total Damage"
    assert res.key == "total_damage"
    assert res.tags == ["offense", "summary"]
    assert res.value == 100.0


def test_sum_down_contribution_should_return_total_down_contribution_in_model_structure():
    all_stats_logs = [
        get_stub_player_misc_stats(downContribution=24.5),
        get_stub_player_misc_stats(downContribution=25.50),
        get_stub_player_misc_stats(downContribution=50),
    ]

    res = sum_down_contribution(all_stats_logs)

    assert isinstance(res, AggregatedPlayerStat)
    assert res.friendly_name == "Total Down Contribution"
    assert res.key == "total_down_contribution"
    assert res.tags == ["offense", "summary"]
    assert res.value == 100.0
