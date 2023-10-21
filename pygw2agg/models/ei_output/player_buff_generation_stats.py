from pydantic import BaseModel


class PlayerBuffGenerationStats(BaseModel):
    generation: int
    overstack: int
    wasted: int
    unknownExtended: int
    byExtension: int
    extended: int
