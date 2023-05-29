from sqlalchemy.orm import Session
from models.cooperative import Cooperative
from schemas.cooperative import CooperativeCreate


def get_user(db: Session, user_id: int):
    return db.query(Cooperative).filter(Cooperative.id == user_id).first()


def create_user(db: Session, user: CooperativeCreate):
    pass
