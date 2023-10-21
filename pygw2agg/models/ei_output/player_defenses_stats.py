from pydantic import BaseModel


class PlayerDefensesStats(BaseModel):
    damageTaken: int
    breakbarDamageTaken: int
    blockedCount: int
    evadedCount: int
    missedCount: int
    dodgeCount: int
    invulnedCount: int
    damageBarrier: int
    interruptedCount: int
    downCount: int
    downDuration: int
    deadCount: int
    deadDuration: int
    dcCount: int
    dcDuration: int
