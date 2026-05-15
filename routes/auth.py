from fastapi import APIRouter , Depends
from fastapi.security import OAuth2PasswordRequestForm
from core.database import get_db
from sqlalchemy.orm import Session
from models.user_model import User
from utils.response import api_response
from auth.hashing import verify_password
from auth.jwt_handler import create_access_token


router = APIRouter(tags=["Auth"])

@router.post("/login")
def log_in (
    request : OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        user = db.query(User).filter (
            User.email == request.username
        ).first()

        if not user :
            return api_response(
            status_code=401,
            message="Invalid email",
            data={},
            success=False   
            )
        
        valid_pass = verify_password(
            request.password ,
            user.hashed_password
        )

        if not valid_pass :
            return api_response(
            status_code=401,
            message="Invalid password",
            data={},
            success=False   
            )
        
        access_token = create_access_token(
            {"sub" : user.email}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
            }
    except Exception as e:
        print(f"Error occurred in login route: {e}")
        return api_response(
            status_code=500,
            message="Internal server error",
            data={},
            success=False
        )