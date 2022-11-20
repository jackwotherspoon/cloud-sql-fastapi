from typing import Union

from datetime import datetime
from pydantic import BaseModel


class ExpenseBase(BaseModel):
    cost: float
    description: Union[str, None] = None
    category: str = "Misc"


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    expense_id: int
    time_created: datetime

    class Config:
        orm_mode = True
