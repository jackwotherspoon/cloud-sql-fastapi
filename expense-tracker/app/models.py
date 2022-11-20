from sqlalchemy import Column, DateTime, Integer, String, Float

from .database import Base


class Expense(Base):
    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime, index=True, nullable=False)
    cost = Column(Float, nullable=False)
    description = Column(String(30), nullable=True)
    category = Column(String(30), nullable=True)
