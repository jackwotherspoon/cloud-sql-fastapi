from typing import Union, Optional

from datetime import datetime
from pydantic import BaseModel


class ExpenseBase(BaseModel):
    cost: float
    description: Union[str, None] = None
    category: str = "Misc"


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    cost: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None


class Expense(ExpenseBase):
    expense_id: int
    time_created: datetime

    class Config:
        orm_mode = True
