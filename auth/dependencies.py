from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from auth.jwt_handler import verify_access_token
from models.user_model import User
from jose import JWTError


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







