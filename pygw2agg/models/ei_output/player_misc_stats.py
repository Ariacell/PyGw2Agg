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


def get_stub_player_misc_stats(
    wasted=43.123,
    timeWasted=43.123,
    saved=43.123,
    timeSaved=43.123,
    stackDist=43.123,
    distToCom=43.123,
    avgBoons=43.123,
    avgActiveBoons=43.123,
    avgConditions=43.123,
    avgActiveConditions=43.123,
    swapCount=43.123,
    totalDamageCount=43.123,
    directDamageCount=43.123,
    connectedDirectDamageCount=43.123,
    connectedDamageCount=43.123,
    downContribution=43.123,
    critableDirectDamageCount=43.123,
    criticalRate=43.123,
    criticalDmg=43.123,
    flankingRate=43.123,
    againstMovingRate=43.123,
    glanceRate=43.123,
    missed=43.123,
    evaded=4,
    blocked=4,
    interrupts=4,
    invulned=4,
    killed=4,
    downed=4,
):
    return PlayerMiscStats(
        wasted=wasted,
        timeWasted=timeWasted,
        saved=saved,
        timeSaved=timeSaved,
        stackDist=stackDist,
        distToCom=distToCom,
        avgBoons=avgBoons,
        avgActiveBoons=avgActiveBoons,
        avgConditions=avgConditions,
        avgActiveConditions=avgActiveConditions,
        swapCount=swapCount,
        totalDamageCount=totalDamageCount,
        directDamageCount=directDamageCount,
        connectedDirectDamageCount=connectedDirectDamageCount,
        connectedDamageCount=connectedDamageCount,
        downContribution=downContribution,
        critableDirectDamageCount=critableDirectDamageCount,
        criticalRate=criticalRate,
        criticalDmg=criticalDmg,
        flankingRate=flankingRate,
        againstMovingRate=againstMovingRate,
        glanceRate=glanceRate,
        missed=missed,
        evaded=evaded,
        blocked=blocked,
        interrupts=interrupts,
        invulned=invulned,
        killed=killed,
        downed=downed,
    )
