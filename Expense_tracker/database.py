from sqlalchemy import orm, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "oracle+oracledb://system:Hello%4011@localhost:1521/XE"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


