from sqlalchemy import Column, String, DateTime, Integer
from dataclasses import dataclass

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
    visits = Column(Integer, nullable=True, Default = 1)