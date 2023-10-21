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
