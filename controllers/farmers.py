from sqlalchemy.orm import Session
from models.farmers import Farmers
from schemas.farmers import FarmersCreate


def get_user(db: Session, user_id: int):
    return db.query(Farmers).filter(Farmers.id == user_id).first()


def create_user(db: Session, user: FarmersCreate):
    pass
