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
