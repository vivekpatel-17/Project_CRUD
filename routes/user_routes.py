from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services import user_services
from schemas.user_schemas import UserCreate
from utils.response import api_response
router = APIRouter(tags=["Users"])

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = user_services.get_all_users(db)  
    try:
        return api_response(
            status_code=200,
            message="Users fetched successfully",
            data=users,
            success=True
        )
    except Exception as e:
        print(f"Error occurred while fetching users: {e}")
        return api_response(
            status_code=500,
            message="unexpected error happened",
            data= None,
            success= False
        )

@router.get("/user/{id}")
def get_user_by_id(id: int ,db: Session = Depends(get_db)):
    user = user_services.get_user_by_id(db, id)
    try:
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
    except Exception as e:
        print(f"Error occurred while fetching user: {e}")
        return api_response(
            status_code=500,
            message="unexpected error happened",
            data= None,
            success= False
        )

@router.post("/user")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    try:

        created_user = user_services.create_user(
            db,
            user
        )

        if not created_user:

            return api_response(
                status_code=400,
                message="User creation failed",
                data=None,
                success=False
            )

        return api_response(
            status_code=201,
            message="User created successfully",
            data=created_user,
            success=True
        )

    except Exception as e:

        print(f"Error occurred while creating user: {e}")

        return api_response(
            status_code=500,
            message="Unexpected error happened",
            data=None,
            success=False
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
    try:
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
    except Exception as e:
        print(f"Error occurred while fetching user: {e}")
        return api_response(
            status_code=500,
            message="unexpected error happened",
            data= None,
            success= False
        )