
from fastapi import FastAPI
from core.database import  engine 
from models.user_model import Base
from routes.user_routes import router as user_router
from routes.task_routes import router as task_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(task_router)
@app.get("/")
def read_root():
    
    return {"message": "Welcome to the User API!"}
