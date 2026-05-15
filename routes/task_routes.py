from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services import tasks_services
from schemas.schemas_taks import TaskCreate
from utils.response import api_response
from auth.dependencies import get_current_user
router = APIRouter(tags=["Tasks"])

@router.get("/tasks")
def get_all_task(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)):
    tasks = tasks_services.get_all_task(db)  
    try:
        return api_response(
            status_code=200,
            message="tasks fetched successfully",
            data=tasks,
            success=True
        )
    except Exception as e:
        print(f"Error occurred while fetching tasks: {e}")
        return api_response(
            status_code=500,
            message="unexpected error happened",
            data= None,
            success= False
        )

@router.get("/tasks/{id}")
def get_task_by_id(id: int ,db: Session = Depends(get_db)):
    user = tasks_services.get_task_by_id(db, id)
    try:
        if user:
            return api_response(
                status_code=200,
                message="task fetched successfully",
                data=user,
                success=True
            )
        else:
            return api_response(
                status_code=404,
                message="task not found",
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

@router.post("/tasks")
def create_task(task:TaskCreate, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    try:
        task = tasks_services.create_task(db, task)
        return api_response(
            status_code=200,
            message="task created successfully",
            data=task,
            success=True
        )
    except Exception as e:
        print(f"Error occurred while fetching task: {e}")
        return api_response(
            status_code=500,
            message="unexpected error happened",
            data= None,
            success= False
        )


@router.put("/tasks/{id}")
def update_task(id: int, task: TaskCreate, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    user = tasks_services.update_task(db, id, task)
    if user:
        return api_response(
            status_code=200,
            message="User updated successfully",
            data=task,
            success=True
        )
    else:
        return api_response(
            status_code=404,
            message="User not found",
            data=None,
            success=False
        )

@router.delete("/task/{id}")    
def delete_user(id: int, db: Session = Depends(get_db)):

    deleted = tasks_services.delete_task(db, id)
    try:
        if deleted:
            return api_response(
                status_code=200,
                message="task deleted successfully",
                data=None,
                success=True
            )
        else:
            return api_response(
                status_code=404,
                message="task not found",
                data=None,
                success=False
            )
    except Exception as e:
        print(f"Error occurred while fetching task: {e}")
        return api_response(
            status_code=500,
            message="unexpected error happened",
            data= None,
            success= False
        )