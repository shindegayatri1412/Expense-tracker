from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Numeric, CLOB
import datetime



class ExpUserDetails(Base):
    __tablename__ = "EXP_USER_DETAILS"

    id = Column(Integer, primary_key = True)
    email = Column(String(100), nullable= False)
    first_name= Column(String(500))
    last_name = Column(String(50))
    salary= Column(Integer)
    saving_limit = Column(Integer)
    start_date = Column(DateTime, default=datetime.date.today())
    available_balance = Column(Integer)
    daily_limit = Column(Integer)




class ExpEntry(Base):
    __tablename__ = "EXP_ENTRY"

    id = Column(Integer, primary_key = True)
    exp_user_id = Column(Integer, nullable= False)
    created_on = Column(DateTime, default=datetime.date.today())
    exp_details = Column(CLOB)
    total_expense = Column(Integer)

