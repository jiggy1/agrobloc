from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    pass


def get_user_by_cellphone(db: Session, cellphone: int):
    pass


def create_user(db: Session, user: UserCreate):
    pass
