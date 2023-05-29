from sqlalchemy.orm import Session
from models.factory import Factory
from schemas.factory import FactoryCreate


def get_user(db: Session, user_id: int):
    return db.query(Factory).filter(Factory.id == user_id).first()


def create_user(db: Session, user: FactoryCreate):
    pass
