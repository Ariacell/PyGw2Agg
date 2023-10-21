from decimal import Decimal
from pydantic import BaseModel


class PlayerDefensesStats(BaseModel):
    damageTaken: Decimal
    breakbarDamageTaken: Decimal
    blockedCount: Decimal
    evadedCount: Decimal
    missedCount: Decimal
    dodgeCount: Decimal
    invulnedCount: Decimal
    damageBarrier: Decimal
    interruptedCount: Decimal
    downCount: Decimal
    downDuration: Decimal
    deadCount: Decimal
    deadDuration: Decimal
    dcCount: Decimal
    dcDuration: Decimal
