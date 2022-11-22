from datetime import datetime, timezone

from sqlalchemy.orm import Session
from sqlalchemy import desc

from . import models, schemas


def get_expenses(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Expense)
        .order_by(desc("time_created"))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_exepense_by_id(db: Session, expense_id: int):
    return (
        db.query(models.Expense).filter(models.Expense.expense_id == expense_id).first()
    )


def create_expense(db: Session, expense: schemas.ExpenseCreate):
    new_expense = models.Expense(
        time_created=datetime.now(tz=timezone.utc), **expense.dict()
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def delete_expense(db: Session, expense_id: int):
    db.query(models.Expense).filter(models.Expense.expense_id == expense_id).delete()
    db.commit()
    return
