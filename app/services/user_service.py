from app.models import SessionLocal, User
from fastapi import Depends
from app.schemas import User
from sqlalchemy.orm import Session
from app.services import authentication

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(token: str = Depends(authentication.get_token)):
    return authentication.auth_scheme(token)

def get_current_user(db: Session, token: str):
    return authentication.get_current_user(db, token)
