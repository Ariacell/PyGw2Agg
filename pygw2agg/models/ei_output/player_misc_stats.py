from decimal import Decimal
from pydantic import BaseModel


class PlayerMiscStats(BaseModel):
    wasted: Decimal
    timeWasted: Decimal
    saved: Decimal
    timeSaved: Decimal
    stackDist: Decimal
    distToCom: Decimal
    avgBoons: Decimal
    avgActiveBoons: Decimal
    avgConditions: Decimal
    avgActiveConditions: Decimal
    swapCount: Decimal
    totalDamageCount: Decimal
    directDamageCount: Decimal
    connectedDirectDamageCount: Decimal
    connectedDamageCount: Decimal
    downContribution: Decimal
    critableDirectDamageCount: Decimal
    criticalRate: Decimal
    criticalDmg: Decimal
    flankingRate: Decimal
    againstMovingRate: Decimal
    glanceRate: Decimal
    missed: Decimal
    evaded: int
    blocked: int
    interrupts: int
    invulned: int
    killed: int
    downed: int
