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


def get_stub_player_defenses_stats(
    damageTaken=52.342,
    breakbarDamageTaken=52.342,
    blockedCount=52.342,
    evadedCount=52.342,
    missedCount=52.342,
    dodgeCount=52.342,
    invulnedCount=52.342,
    damageBarrier=52.342,
    interruptedCount=52.342,
    downCount=52.342,
    downDuration=52.342,
    deadCount=52.342,
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
