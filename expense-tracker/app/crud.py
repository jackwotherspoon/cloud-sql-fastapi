from datetime import datetime, timezone

from fastapi import HTTPException
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


def get_expense_by_id(db: Session, expense_id: int):
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


def update_expense(
    db: Session, expense_id: int, expense_partial: schemas.ExpenseUpdate
):
    expense = (
        db.query(models.Expense).filter(models.Expense.expense_id == expense_id).first()
    )
    expense_data = expense_partial.dict(exclude_unset=True)
    for key, value in expense_data.items():
        setattr(expense, key, value)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def delete_expense(db: Session, expense_id: int):
    expense = (
        db.query(models.Expense).filter(models.Expense.expense_id == expense_id).first()
    )
    if expense:
        db.delete(expense)
        db.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"Expense not found with ID {expense_id}"
        )
