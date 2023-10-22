from pydantic import BaseModel, ConfigDict


class BaseAggregatedModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
