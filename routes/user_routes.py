from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services import user_services
from schemas.user_schemas import UserCreate
from utils.response import api_response
router = APIRouter()

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = user_services.get_all_users(db)  
    return api_response(
        status_code=200,
        message="Users fetched successfully",
        data=users,
        success=True
    )

@router.get("/user/{id}")
def get_user_by_id(id: int ,db: Session = Depends(get_db)):
    user = user_services.get_user_by_id(db, id)
    if user:
        return api_response(
            status_code=200,
            message="User fetched successfully",
            data=user,
            success=True
        )
    else:
        return api_response(
            status_code=404,
            message="User not found",
            data=None,
            success=False
        )

@router.post("/user")
def create_user(user:UserCreate, db: Session = Depends(get_db)):
    user = user_services.create_user(db, user)
    return api_response(
        status_code=200,
        message="User created successfully",
        data=user,
        success=True
    )

@router.put("/user/{id}")
def update_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    user = user_services.update_user(db, id, user)
    if user:
        return api_response(
            status_code=200,
            message="User updated successfully",
            data=user,
            success=True
        )
    else:
        return api_response(
            status_code=404,
            message="User not found",
            data=None,
            success=False
        )

@router.delete("/user/{id}")    
def delete_user(id: int, db: Session = Depends(get_db)):
    deleted = user_services.delete_user(db, id)
    if deleted:
        return api_response(
            status_code=200,
            message="User deleted successfully",
            data=None,
            success=True
        )
    else:
        return api_response(
            status_code=404,
            message="User not found",
            data=None,
            success=False
        )
