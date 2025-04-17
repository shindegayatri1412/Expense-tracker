from database import SessionLocal
from model import *
from fastapi import HTTPException
import json


db = SessionLocal()


def create_user_entry(req):
    user_details = db.query(ExpUserDetails).filter(ExpUserDetails.email == req.email).first()
    if user_details:
        raise HTTPException(status_code=400, detail="User already exists")

    user_entry = ExpUserDetails(
        email = req.email,
        first_name = req.first_name,
        last_name = req.last_name,
        salary= req.salary,
        saving_limit= req.saving_limit,
        start_date = datetime.date.today()
    )

    db.add(user_entry)
    db.commit()

    return True

def daily_expense_entry(req):
    print("req type1 =======",type(req))
    req= req.dict()
    print("req type2 =======",type(req))
    print("req  =======",req)

    req_exp_dict = {}
    for i in req["expense_details"]:
        req_exp_dict[i["expense_name"]] = i["expense_ammout"]

    print("req_exp_dict======",req_exp_dict)


    user_details = db.query(ExpUserDetails).filter(ExpUserDetails.email == req["email"]).first()

    if not user_details:
        raise HTTPException(status_code= 400, detail= "User does not exist!")

    exp_entry_details = db.query(ExpEntry).filter(ExpEntry.exp_user_id == user_details.id, 
                                            ExpEntry.created_on == datetime.date.today()).first()
    
    if not exp_entry_details:
        expense_entry = ExpEntry(
            exp_user_id = user_details.id,
            created_on = datetime.date.today(),
            exp_details = json.dumps(req_exp_dict))
        db.add(expense_entry)
        db.commit()

    else:
        exp_details_dict = json.loads(exp_entry_details.exp_details)
        exp_details_dict.update(req_exp_dict)
        exp_entry_details.exp_details = json.dumps(exp_details_dict)
        db.commit()
        

    return True
    
