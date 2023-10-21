from pydantic import BaseModel, ConfigDict


class BaseEiJsonModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
