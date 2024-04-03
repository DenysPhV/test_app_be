from fastapi import APIRouter, Depends 
from app.schemas import Post, PostCreate
from app.services import post_service
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/addpost/", response_model=Post)
def add_post(post: PostCreate, token: str = Depends(post_service.verify_token), db: Session = Depends(post_service.get_db)):
    return post_service.create_post(db, post, token)

@router.get("/getposts/", response_model=list[Post])
def get_posts(token: str = Depends(post_service.verify_token), db: Session = Depends(post_service.get_db)):
    return post_service.get_user_posts(db, token)

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, token: str = Depends(post_service.verify_token), db: Session = Depends(post_service.get_db)):
    return post_service.delete_post(db, post_id, token)
