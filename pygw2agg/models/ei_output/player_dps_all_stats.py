from pydantic import BaseModel


class PlayerDpsAllStats(BaseModel):
    dps: int
    damage: int
    condiDps: int
    condiDamage: int
    powerDps: int
    powerDamage: int
    breakbarDamage: int
    actorDps: int
    actorDamage: int
    actorCondiDps: int
    actorCondiDamage: int
    actorPowerDps: int
    actorPowerDamage: int
    actorBreakbarDamage: int
