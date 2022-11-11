from typing import List

from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, HTTPException, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request, db: Session = Depends(get_db)):
    tab_count = crud.get_vote_count(db, "TABS")
    space_count = crud.get_vote_count(db, "SPACES")
    votes = crud.get_recent_votes(db)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tab_count": tab_count,
            "space_count": space_count,
            "recent_votes": votes,
        },
    )


@app.get("/votes", response_model=List[schemas.Vote])
def get_votes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recent_votes(db, skip=skip, limit=limit)


@app.post("/votes", response_model=schemas.Vote)
def create_vote(candidate: str = Form(), db: Session = Depends(get_db)):
    if candidate != "SPACES" and candidate != "TABS":
        raise HTTPException(
            status_code=400,
            detail="Invalid candidate specified. Should be one of 'TABS' or 'SPACES'",
        )
    return crud.create_vote(db, candidate)
