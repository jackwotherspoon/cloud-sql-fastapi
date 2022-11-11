from datetime import datetime
from pydantic import BaseModel


class Vote(BaseModel):
    candidate: str
    time_cast: datetime

    class Config:
        orm_mode = True
