from decimal import Decimal
from pydantic import BaseModel


class PlayerDefensesStats(BaseModel):
    damageTaken: int
    breakbarDamageTaken: Decimal
    blockedCount: Decimal
    evadedCount: Decimal
    missedCount: int
    dodgeCount: int
    invulnedCount: Decimal
    damageBarrier: Decimal
    interruptedCount: int
    downCount: int
    downDuration: Decimal
    deadCount: int
    deadDuration: Decimal
    dcCount: Decimal
    dcDuration: Decimal


def get_stub_player_defenses_stats(
    damageTaken=52,
    breakbarDamageTaken=52.342,
    blockedCount=52.342,
    evadedCount=52.342,
    missedCount=52,
    dodgeCount=52,
    invulnedCount=52.342,
    damageBarrier=52.342,
    interruptedCount=52,
    downCount=52,
    downDuration=52.342,
    deadCount=52,
    deadDuration=52.342,
    dcCount=52.342,
    dcDuration=52.342,
):
    return PlayerDefensesStats(
        damageTaken=damageTaken,
        breakbarDamageTaken=breakbarDamageTaken,
        blockedCount=blockedCount,
        evadedCount=evadedCount,
        missedCount=missedCount,
        dodgeCount=dodgeCount,
        invulnedCount=invulnedCount,
        damageBarrier=damageBarrier,
        interruptedCount=interruptedCount,
        downCount=downCount,
        downDuration=downDuration,
        deadCount=deadCount,
        deadDuration=deadDuration,
        dcCount=dcCount,
        dcDuration=dcDuration,
    )
