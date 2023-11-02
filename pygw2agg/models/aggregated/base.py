from enum import Enum
from pydantic import BaseModel, ConfigDict


class BaseAggregatedModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class STAT_TAGS_ENUM(str, Enum):
    common = "common"
    summary = "summary"
    defense = "defense"
    utility = "utility"
    offense = "offense"
    support = "support"
