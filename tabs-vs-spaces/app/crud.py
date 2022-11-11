from datetime import datetime, timezone

from sqlalchemy.orm import Session
from sqlalchemy import desc

from . import models


def get_recent_votes(db: Session, skip: int = 0, limit: int = 5):
    return (
        db.query(models.Vote)
        .order_by(desc("time_cast"))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_vote_count(db: Session, candidate: str):
    return db.query(models.Vote).filter(models.Vote.candidate == candidate).count()


def create_vote(db: Session, candidate: str):
    new_vote = models.Vote(time_cast=datetime.now(tz=timezone.utc), candidate=candidate)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote
