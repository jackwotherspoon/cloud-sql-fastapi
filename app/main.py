from typing import List
from datetime import datetime, timezone

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/votes", response_model=List[schemas.Vote])
def get_votes(db: Session = Depends(get_db)):
    return db.query(models.Vote).all()


@app.post("/votes", response_model=schemas.Vote)
def create_vote(vote: schemas.VoteCreate, db: Session = Depends(get_db)):
    # convert to lowercase to allow for 'TABS' or 'tabs"
    candidate = vote.candidate.lower()
    if candidate != "spaces" and candidate != "tabs":
        raise HTTPException(status_code=400, detail="Invalid team specified. Should be one of 'TABS' or 'SPACES'")
    new_vote = models.Vote(time_cast=datetime.now(tz=timezone.utc), candidate=candidate)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote
