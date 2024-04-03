from app.models import SessionLocal, Post
from fastapi import Depends, HTTPException, status
from app.schemas import PostCreate
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

def create_post(db: Session, post: PostCreate, token: str):
    user = authentication.get_current_user(db, token)
    db_post = Post(text=post.text, user_id=user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_user_posts(db: Session, token: str):
    user = authentication.get_current_user(db, token)
    return db.query(Post).filter(Post.user_id == user.id).all()

def delete_post(db: Session, post_id: int, token: str):
    user = authentication.get_current_user(db, token)
    post = db.query(Post).filter(Post.id == post_id).first()
    if post.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to delete this post")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}
