from sqlalchemy import Column, String, DateTime, Integer
from dataclasses import dataclass
import re

from sqlalchemy.sql.expression import true

from app.configs.database import db

@dataclass
class LeadModel(db.Model):
    id: int
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "lead_info"
  

    id =  Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime, nullable=True)
    last_visit = Column(DateTime, nullable=True)
    visits = Column(Integer, nullable=True, default = 1)

    @staticmethod
    def isPhoneFormated(phone):

        patern = r"^\([0-9]{2}\)[0-9]{5}\-[0-9]{4}$"

        print(f'5>>>>>>>>>>> {type(re.fullmatch(patern, phone, flags=0)) == None }')

        if re.fullmatch(patern, phone, flags=0):
            return True
       



