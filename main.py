from fastapi import FastAPI
from application.schema import *
from application.service import *


app = FastAPI()

@app.get("/chkapi")
def chk_api():
    return "Hello there"

    

@app.post("/create_user")
def create_user(req: CreateUser):
    res = create_user_entry(req)
    return True


@app.post("/daily_expense_entry")
def expense_entry(req: ExpenseEntry):
    res = daily_expense_entry(req)
    return True