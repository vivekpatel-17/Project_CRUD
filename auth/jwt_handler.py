from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from utils.response import api_response

secret_key = os.getenv("secret_key")
ALGORITHM  = os.getenv("ALGORITHM")

ACESS_TOKEN_EXPIRE_TIME = os.getenv("ACESS_TOKEN_EXPIRE_TIME") 

def create_access_token(data:dict):
    try:
        to_encode = data.copy()

        expire = datetime.now(timezone.utc)+timedelta(minutes=ACESS_TOKEN_EXPIRE_TIME)

        to_encode.update({
            "exp":expire
        })

        encode_jwt = jwt.encode(
            to_encode , secret_key , algorithm=ALGORITHM
        )
        return encode_jwt
    except Exception as e:
        print(f"Error occurred while creating access token: {e}")
        return api_response(
            status_code=500,    
            message="unexpected error happened",
            data= None,
            success= False
        )
    


def verify_access_token(token:str):
    try :
        payload = jwt.decode(
            token , secret_key , algorithms=[ALGORITHM]
        )
        print(payload)
        return payload 
    except JWTError:
        return api_response(
            status_code=401,    
            message="Invalid or expired token",
            data= None,
            success= False
        )