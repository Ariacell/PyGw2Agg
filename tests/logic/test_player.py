from pygw2agg.logic.player import aggregate_player_logs
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.common.professions import ProfessionEnum
from pygw2agg.models.ei_output.log_data import get_stub_log
from pygw2agg.models.ei_output.player import get_stub_player_stats


class TestAggregatePlayerLogs:
    test_player_name = "Magnus"
    test_player_account = "Magnus.1234"
    test_player_profession = ProfessionEnum.firebrand.value

    test_log_1 = get_stub_log(
        players=[
            get_stub_player_stats(
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
