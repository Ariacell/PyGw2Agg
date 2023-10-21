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
