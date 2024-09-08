from sqlalchemy import Column, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(String, primary_key=True)
    us_birth_gender = Column(String)
    birth_date = Column(Date)
    family_name = Column(String)
    given_name = Column(String)
    prefix = Column(String)
    contact = Column(String)
