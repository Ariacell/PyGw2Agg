from decimal import Decimal
from pydantic import BaseModel


class PlayerDpsAllStats(BaseModel):
    dps: Decimal
    damage: Decimal
    condiDps: Decimal
    condiDamage: Decimal
    powerDps: Decimal
    powerDamage: Decimal
    breakbarDamage: Decimal
    actorDps: Decimal
    actorDamage: Decimal
    actorCondiDps: Decimal
    actorCondiDamage: Decimal
    actorPowerDps: Decimal
    actorPowerDamage: Decimal
    actorBreakbarDamage: Decimal


def get_stub_player_dps_all_stats(
    dps=52.342,
    damage=52.342,
    condiDps=52.342,
    condiDamage=52.342,
    powerDps=52.342,
    powerDamage=52.342,
    breakbarDamage=52.342,
    actorDps=52.342,
    actorDamage=52.342,
    actorCondiDps=52.342,
    actorCondiDamage=52.342,
    actorPowerDps=52.342,
    actorPowerDamage=52.342,
    actorBreakbarDamage=52.342,
):
    return PlayerDpsAllStats(
        dps=dps,
        damage=damage,
        condiDps=condiDps,
        condiDamage=condiDamage,
        powerDps=powerDps,
        powerDamage=powerDamage,
        breakbarDamage=breakbarDamage,
        actorDps=actorDps,
        actorDamage=actorDamage,
        actorCondiDps=actorCondiDps,
        actorCondiDamage=actorCondiDamage,
        actorPowerDps=actorPowerDps,
        actorPowerDamage=actorPowerDamage,
        actorBreakbarDamage=actorBreakbarDamage,
    )
