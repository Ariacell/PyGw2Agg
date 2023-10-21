from pydantic import BaseModel


class PlayerMiscStats(BaseModel):
    wasted: int
    timeWasted: int
    saved: int
    timeSaved: int
    stackDist: int
    distToCom: int
    avgBoons: int
    avgActiveBoons: int
    avgConditions: int
    avgActiveConditions: int
    swapCount: int
    totalDamageCount: int
    directDamageCount: int
    connectedDirectDamageCount: int
    connectedDamageCount: int
    downContribution: int
    critableDirectDamageCount: int
    criticalRate: int
    criticalDmg: int
    flankingRate: int
    againstMovingRate: int
    glanceRate: int
    missed: int
    evaded: int
    blocked: int
    interrupts: int
    invulned: int
    killed: int
    downed: int
