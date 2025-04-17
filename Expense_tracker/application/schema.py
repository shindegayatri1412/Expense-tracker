from pydantic import BaseModel, field_validator
from typing import Optional, List
from datetime import datetime


class CreateUser(BaseModel):
    email: str
    first_name: str
    last_name: str
    salary: int
    saving_limit: Optional[int] = 0


class ExpenseDetails(BaseModel):
    expense_name: str
    expense_ammout: int

class ExpenseEntry(BaseModel):
    email: str
    expense_details: List[ExpenseDetails]
