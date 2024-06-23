from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
from pygw2agg.models.common.professions import ProfessionEnum
from pygw2agg.models.ei_output.base_ei_model import BaseEiJsonModel
from pygw2agg.models.ei_output.player_buff_generation_stats import (
    PlayerBuffGenerationStats,
)
from pygw2agg.models.ei_output.player_buff_uptime_stats import PlayerBuffUptimeStats
from pygw2agg.models.ei_output.player_defenses_stats import (
    PlayerDefensesStats,
    get_stub_player_defenses_stats,
)
from pygw2agg.models.ei_output.player_dps_all_stats import (
    PlayerDpsAllStats,
    get_stub_player_dps_all_stats,
)
from pygw2agg.models.ei_output.player_dps_target_stats import (
    PlayerDpsTargetStats,
    get_stub_player_dps_target_stats,
)
from pygw2agg.models.ei_output.player_misc_stats import (
    PlayerMiscStats,
    get_stub_player_misc_stats,
)

from pygw2agg.models.ei_output.player_support_stats import (
    PlayerSupportStats,
    get_stub_player_support_stats,
)


class Player(BaseEiJsonModel):
    account: Optional[str] = None
    name: str
    activeTimes: List[Decimal]
    group: int
    hasCommanderTag: bool
    profession: ProfessionEnum
    friendlyNPC: bool
    notInSquad: bool
    guildID: Optional[str] = None
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


def get_stub_player(
    name="someone",
    account="someone.1234",
    profession=ProfessionEnum.elementalist.value,
    active_times=[12345, 4312],
    support_stats=[get_stub_player_support_stats()],
    dps_all_stats=[get_stub_player_dps_all_stats()],
    dps_target_stats=[[get_stub_player_dps_target_stats()]],
    defenses_stats=[get_stub_player_defenses_stats()],
    misc_stats=[get_stub_player_misc_stats()],
):
    return Player(
        account=account,
        name=name,
        activeTimes=active_times,
        group=1,
        hasCommanderTag=False,
        profession=profession,
        friendlyNPC=False,
        notInSquad=False,
        guildID="432",
        weapons=[{}],
        support=support_stats,
        dpsAll=dps_all_stats,
        dpsTargets=dps_target_stats,  # Dps to targets is a nested array of damage per target, per phase
        defenses=defenses_stats,
        statsAll=misc_stats,
    )
