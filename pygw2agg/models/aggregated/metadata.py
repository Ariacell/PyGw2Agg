from pydantic import BaseModel


class AggregateMetadata(BaseModel):
    start_time: str
    end_time: str
