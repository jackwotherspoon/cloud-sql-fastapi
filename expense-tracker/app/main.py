from typing import List

from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from . import models, schemas, crud
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


@app.get("/expenses/", response_model=List[schemas.Expense])
def get_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_expenses(db, skip=skip, limit=limit)


@app.get("/expenses/{expense_id}", response_model=schemas.Expense)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.get_exepense_by_id(db, expense_id)


@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)


@app.delete("/expenses/{expense_id}", response_class=Response)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    crud.delete_expense(db, expense_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
