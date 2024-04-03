from fastapi import APIRouter, Depends
from app.services import user_service
from app.schemas import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/me/", response_model=User)
def read_users_me(token: str = Depends(user_service.verify_token), db: Session = Depends(user_service.get_db)):
    return user_service.get_current_user(db, token)
