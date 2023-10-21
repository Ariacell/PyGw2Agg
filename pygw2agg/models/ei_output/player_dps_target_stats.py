from pydantic import BaseModel


class PlayerDpsTargetStats(BaseModel):
    dps: int
    damage: int
    condiDps: int
    condiDamage: int
    powerDps: int
    powerDamage: int
    breakbarDamage: int
