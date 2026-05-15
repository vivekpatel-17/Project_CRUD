from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from auth.jwt_handler import verify_access_token
from models.user_model import User
from jose import JWTError
from models.tasks_model import Task
from models.user_task import UserTaskMapping


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl = "login"
)

def get_current_user(
        token:str = Depends(oauth2_scheme),
        db:Session = Depends(get_db)
):
    try: 
        payload = verify_access_token(token)

        if not payload :
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )
        email = payload.get("sub")
        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user: 
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    

def admin_required(
        current_user = Depends(get_current_user)
):
    if current_user.role != "admin" : 
        raise HTTPException(
            status_code=403,
            detail = "admin access required"
        )
    return current_user


def task_access_required (
        task_id : int ,
        db:Session = Depends(get_db),
        current_user = Depends(get_current_user)
):
    try :
        if current_user.role == "admin":
            task = db.query(Task).filter(
                Task.id == task.id
            ).first()

        if not task:

                raise HTTPException(
                    status_code=404,
                    detail="Task not found"
                )

        return task
    
        mapping= db.query(UserTaskMapping).filter(

           UserTaskMapping.task_id == task_id,
           UserTaskMapping.user_id == current_user.id 
        ).first()

        
        if not mapping:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )
        
        task = db.query(Task).filter(
            Task.id == task_id
        ).first()

        if not task : 
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return task
    except HTTPException:

        raise

    except Exception as e:

        print(f"Error checking task access: {e}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )





