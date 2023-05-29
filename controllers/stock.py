from sqlalchemy.orm import Session
from models.stock import Stock
from schemas.cooperative import StockCreate


def get_user(db: Session, user_id: int):
    return db.query(Stock).filter(Stock.id == user_id).first()


def create_user(db: Session, user: StockCreate):
    pass
