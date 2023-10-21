from typing import Dict

from pydantic import BaseModel


class PlayerBuffUptimeStats(BaseModel):
    uptime: int
    presence: int
    generated: Dict[str, int]
    overstacked: Dict[str, int]
    wasted: Dict[str, int]
    unknownExtended: Dict[str, int]
    byExtension: Dict[str, int]
    extended: Dict[str, int]
