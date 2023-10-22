from pygw2agg.logic.main import (
    get_logs_lists_per_player,
    get_unique_players_for_log_set,
)
from pygw2agg.models.ei_output.log_data import LogData
from pygw2agg.models.ei_output.player import Player, get_stub_player_stats


class TestLogSorting:
    log_1 = LogData(
        duration="sometime",
        recordedBy="someone",
        timeStart="yesterday",
        players=[
            get_stub_player_stats(name="billy"),
            get_stub_player_stats(name="jean"),
        ],
    )

    log_2 = LogData(
        duration="sometime",
        recordedBy="someone",
        timeStart="yesterday",
        players=[get_stub_player_stats("jean")],
    )

    def get_sample_validated_logs(self):
        return [
            self.log_1,
            self.log_2,
        ]

    def test_should_get_unique_set_of_player_names(self):
        deduped_player_names = get_unique_players_for_log_set(
            self.get_sample_validated_logs()
        )
        assert deduped_player_names == {"billy", "jean"}

    def test_should_get_all_player_logs_for_each_player_by_name(self):
        logs_list = get_logs_lists_per_player(
            ["billy", "jean"], self.get_sample_validated_logs()
        )
        assert logs_list[0] == [self.log_1]
        assert logs_list[1] == [self.log_1, self.log_2]
