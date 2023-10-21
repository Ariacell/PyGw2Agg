from decimal import Decimal
from typing import List
from pydantic import BaseModel
from pygw2agg.models.ei_output.base_ei_model import BaseEiJsonModel
from pygw2agg.models.ei_output.player_buff_generation_stats import (
    PlayerBuffGenerationStats,
)
from pygw2agg.models.ei_output.player_buff_uptime_stats import PlayerBuffUptimeStats
from pygw2agg.models.ei_output.player_defenses_stats import PlayerDefensesStats
from pygw2agg.models.ei_output.player_dps_all_stats import PlayerDpsAllStats
from pygw2agg.models.ei_output.player_dps_target_stats import PlayerDpsTargetStats
from pygw2agg.models.ei_output.player_misc_stats import PlayerMiscStats

from pygw2agg.models.ei_output.player_support_stats import PlayerSupportStats


class Player(BaseEiJsonModel):
    account: str
    name: str
    activeTimes: List[Decimal]
    group: int
    hasCommanderTag: bool
    # profession: PlayerProfessions
    friendlyNPC: bool
    notInSquad: bool
    guildID: str
    weapons: List[object]
    support: List[PlayerSupportStats]
    dpsAll: List[PlayerDpsAllStats]
    dpsTargets: List[
        List[PlayerDpsTargetStats]
    ]  # Dps to targets is a nested array of damage per target, per phase
    defenses: List[PlayerDefensesStats]
    statsAll: List[PlayerMiscStats]
    # buffUptimes: List[PlayerBuffUptimeStats]
    # groupBuffs: List[PlayerBuffGenerationStats]
    # squadBuffs: List[PlayerBuffGenerationStats]
