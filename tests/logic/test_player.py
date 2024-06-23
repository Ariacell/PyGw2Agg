from unittest.mock import patch
from pygw2agg.logic.player import (
    aggregate_player_logs,
    get_player_averages_stats,
    get_player_total_active_time,
    get_player_totals_stats,
)
from pygw2agg.models.aggregated.defense import (
    TotalDamageTaken,
    TotalDeaths,
    TotalDodgeCount,
    TotalTimesDowned,
)
from pygw2agg.models.aggregated.offense import TotalDamage, TotalDownContribution
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregatedPlayerStat
from pygw2agg.models.aggregated.support import (
    AvgCleanses,
    AvgResurrectTime,
    AvgResurrects,
    TotalCleanses,
    TotalResurrectTime,
    TotalResurrects,
)
from pygw2agg.models.aggregated.utility import TotalInterrupts, TotalStrips
from pygw2agg.models.common.professions import ProfessionEnum
from pygw2agg.models.domain.individual_player_log import get_stub_individual_player_log
from pygw2agg.models.ei_output.log_data import (
    get_stub_log,
    to_individual_player_log_data,
)
from pygw2agg.models.ei_output.player import get_stub_player
from pygw2agg.models.ei_output.player_defenses_stats import (
    get_stub_player_defenses_stats,
)
from pygw2agg.models.ei_output.player_support_stats import get_stub_player_support_stats


class TestAggregatePlayerLogs:
    test_player_name = "Magnus"
    test_player_account = "Magnus.1234"
    test_player_profession = ProfessionEnum.firebrand.value

    test_log_1 = get_stub_log(
        players=[
            get_stub_player(
                name=test_player_name,
                account=test_player_account,
                profession=test_player_profession,
            )
        ]
    )

    def test_should_return_model_with_basic_player_info(self):
        aggregate_player = aggregate_player_logs(
            player_name=self.test_player_name, logs=[self.test_log_1]
        )

        assert isinstance(aggregate_player, AggregatedPlayer)
        assert aggregate_player.account == self.test_player_account
        assert aggregate_player.profession == self.test_player_profession
        assert aggregate_player.name == self.test_player_name


class TestGetPlayerTotals:
    test_player_name = "Magnus"
    test_player_account = "Magnus.1234"
    test_player_profession = ProfessionEnum.firebrand.value
    test_log_1 = get_stub_log(
        players=[
            get_stub_player(
                name=test_player_name,
                account=test_player_account,
                profession=test_player_profession,
                support_stats=[get_stub_player_support_stats(resurrects=7)],
            )
        ]
    )
    test_log_2 = get_stub_log(
        players=[
            get_stub_player(
                name=test_player_name,
                account=test_player_account,
                profession=test_player_profession,
                support_stats=[get_stub_player_support_stats(resurrects=5)],
            )
        ]
    )
    test_logs = [test_log_1, test_log_2]
    test_individual_data = list(
        map(to_individual_player_log_data(player_name=test_player_name), test_logs)
    )

    def test_gets_total_player_active_time(self):
        test_log_1 = get_stub_individual_player_log(
            player=get_stub_player(active_times=[40, 20.0])
        )
        test_log_2 = get_stub_individual_player_log(
            player=get_stub_player(active_times=[60, 10.0])
        )

        assert get_player_total_active_time([test_log_1, test_log_2]) == 130

    # Todo: implement additional mocking for individual methods called to collate totals stats
    def test_get_player_totals_stats_should_not_crash(self):
        result = get_player_totals_stats(
            self.test_player_name, self.test_individual_data
        )


class TestGetPlayerAverageStats:
    def get_totals_stats(name: str):
        return [
            TotalCleanses(
                value=120,
            ),
            TotalResurrects(value=30),
            TotalResurrectTime(value=60.0),
            TotalDamage(value=10000),
            TotalDownContribution(value=200),
            TotalDamageTaken(value=1000),
            TotalTimesDowned(value=2),
            TotalDodgeCount(value=16),
            TotalStrips(value=40),
            TotalInterrupts(value=6),
            TotalDeaths(value=1),
        ]

    def test_get_player_averages_stats_should_not_crash(self):
        one_minute_in_ms = 60000
        totals_stats = self.get_totals_stats()
        result = get_player_averages_stats(one_minute_in_ms, totals_stats)
        assert result == [
            AvgCleanses(value=120),
            AvgResurrects(value=30),
            AvgResurrectTime(value=60.0),
        ]
