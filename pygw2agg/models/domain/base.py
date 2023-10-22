from pydantic import BaseModel, ConfigDict


class BaseDomainModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
