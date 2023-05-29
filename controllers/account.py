from sqlalchemy.orm import Session
from models.account import Account
from schemas.account import Account, AccountCreate


def get_user(db: Session, user_id: int):
    return db.query(Account).filter(Account.id == user_id).first()


def create_account(db: Session, user: AccountCreate):
    pass
