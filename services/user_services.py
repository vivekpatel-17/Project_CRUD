from sqlalchemy.orm import Session
from models.user_model import User

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, id: int, user):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return db_user
    return None
    
def delete_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False
