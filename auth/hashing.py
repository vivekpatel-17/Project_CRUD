from passlib.context import CryptContext
from utils.response import api_response

pwd_context = CryptContext(
    schemes = ["bcrypt"] ,
    deprecated = "auto"
)

def hash_password(password:str) :
    try: 
        return pwd_context.hash(password)
    except:
        return api_response(
            status_code=500,    
            message="unexpected error happened",
            data= None,
            success= False
        )
   

def verify_password(
        plain_password : str ,
        hashed_password : str
):
    try:
        return pwd_context.verify(plain_password,hashed_password)
    except:
        return api_response(
            status_code=500,    
            message="unexpected error happened",
            data= None,
            success= False
        )
   