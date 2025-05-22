# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    upload_date = Column(DateTime, default=datetime.utcnow)
    path = Column(String)
