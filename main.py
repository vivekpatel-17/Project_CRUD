
from fastapi import FastAPI
from core.database import  engine , Base 
from routes.user_routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the User API!"}
