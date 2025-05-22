# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    filename: str
    path: str

class DocumentOut(BaseModel):
    id: int
    filename: str
    upload_date: datetime
    path: str

    class Config:
        orm_mode = True

class QueryRequest(BaseModel):
    document_id: int
    question: str

class QueryResponse(BaseModel):
    answer: str