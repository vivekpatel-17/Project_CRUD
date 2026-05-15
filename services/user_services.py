from sqlalchemy.orm import Session
from models.user_model import User
from auth.hashing import hash_password

def get_user_by_id(db: Session, user_id: int):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        print(f"Error occurred while fetching user: {e}")
        return None

def get_all_users(db: Session):
    try:
        return db.query(User).all()
    except Exception as e:
        print(f"Error occurred while fetching users: {e}")
        return None
def create_user(db: Session, user):
    try:
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:

        db.rollback()

        print(f"Error occurred while creating user: {e}")

        return None


def update_user(db: Session, id: int, user):
    try : 
        db_user = db.query(User).filter(User.id == id).first()
       

        if db_user:
            db_user.username = user.username
            db_user.email = user.email
            db_user.hashed_password = user.password
            
            db.commit()
            db.refresh(db_user)
            return db_user
        return None
    
    except Exception as e:
            print(f"Error occurred while fetching user: {e}")
            return None
        
def delete_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    try:
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False
    except Exception as e:
        print(f"Error occurred while fetching user: {e}")
        return False
