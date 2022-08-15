from datetime import datetime
from pydantic import BaseModel


class VoteBase(BaseModel):
    candidate: str


class Vote(VoteBase):
    time_cast: datetime
    
    class Config:
        orm_mode = True


class VoteCreate(VoteBase):
    pass
