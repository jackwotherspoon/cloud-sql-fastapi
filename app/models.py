from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Vote(Base):
    __tablename__ = "votes"

    vote_id = Column(Integer, primary_key=True, index=True)
    time_cast = Column(DateTime, index=True, nullable=False)
    candidate = Column(String(6), nullable=False)
