from pydantic import BaseModel


class PlayerSupportStats(BaseModel):
    resurrects: int
    resurrectTime: int
    condiCleanse: int
    condiCleanseTime: int
    condiCleanseSelf: int
    condiCleanseTimeSelf: int
    boonStrips: int
    boonStripsTime: int
