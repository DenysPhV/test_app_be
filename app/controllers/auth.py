from fastapi import APIRouter, Depends, HTTPException, status
from app.services import authentication
from app.schemas import User, UserCreate
from app.models import User as DBUser
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/signup/", response_model=User)
def signup(user: UserCreate, db: Session = Depends(authentication.get_db)):
    db_user = DBUser(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login/")
def login(email: str, password: str, db: Session = Depends(authentication.get_db)):
    user = authentication.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return {"token": authentication.create_access_token(data={"sub": user.email})}
