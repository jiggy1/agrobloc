from sqlalchemy.orm import Session
from models.dealer import Dealer
from schemas.dealer import DealerCreate


def get_user(db: Session, user_id: int):
    return db.query(Dealer).filter(Dealer.id == user_id).first()


def create_user(db: Session, user: DealerCreate):
    pass
