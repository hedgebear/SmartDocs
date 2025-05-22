# app/routes/upload.py
from fastapi import APIRouter, UploadFile, File, Depends
import shutil, os
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.DocumentOut)
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    doc = models.Document(filename=file.filename, path=file_path)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc