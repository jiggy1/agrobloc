from sqlalchemy.orm import Session
from models.batch import Batch
from schemas.batch import BatchCreate


def get_batch(db: Session, user_id: int):
    return db.query(Batch).filter(Batch.id == user_id).first()


def create_batch(db: Session, user: BatchCreate):
    pass
