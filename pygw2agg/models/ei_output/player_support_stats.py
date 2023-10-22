from decimal import Decimal
from pydantic import BaseModel


class PlayerSupportStats(BaseModel):
    resurrects: int
    resurrectTime: Decimal
    condiCleanse: int
    condiCleanseTime: Decimal
    condiCleanseSelf: int
    condiCleanseTimeSelf: Decimal
    boonStrips: int
    boonStripsTime: Decimal


def get_stub_player_support_stats(
    resurrects=4,
    resurrectTime=20.5,
    condiCleanse=24,
    condiCleanseTime=43.1,
    condiCleanseSelf=12,
    condiCleanseTimeSelf=12.43,
    boonStrips=65,
    boonStripsTime=13.245,
):
    return PlayerSupportStats(
        resurrects=resurrects,
        resurrectTime=resurrectTime,
        condiCleanse=condiCleanse,
        condiCleanseTime=condiCleanseTime,
        condiCleanseSelf=condiCleanseSelf,
        condiCleanseTimeSelf=condiCleanseTimeSelf,
        boonStrips=boonStrips,
        boonStripsTime=boonStripsTime,
    )
