from decimal import Decimal
from pydantic import BaseModel


class PlayerDpsTargetStats(BaseModel):
    dps: Decimal
    damage: Decimal
    condiDps: Decimal
    condiDamage: Decimal
    powerDps: Decimal
    powerDamage: Decimal
    breakbarDamage: Decimal


def get_stub_player_dps_target_stats(
    dps=52.342,
    damage=52.342,
    condiDps=52.342,
    condiDamage=52.342,
    powerDps=52.342,
    powerDamage=52.342,
    breakbarDamage=52.342,
):
    return PlayerDpsTargetStats(
        dps=dps,
        damage=damage,
        condiDps=condiDps,
        condiDamage=condiDamage,
        powerDps=powerDps,
        powerDamage=powerDamage,
        breakbarDamage=breakbarDamage,
    )
