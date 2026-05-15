from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from core.database import get_db

from schemas.user_task_schemas import UserTaskCreate

from services import user_task_services

from utils.response import api_response


router = APIRouter(tags=["Task Assigened"])


@router.post("/assign-task")
def assign_task(
    mapping: UserTaskCreate,
    db: Session = Depends(get_db)
):

    try:

        assigned_task = user_task_services.assign_task_to_user(
            db,
            mapping
        )

        if not assigned_task:

            return api_response(
                status_code=400,
                message="Task assignment failed",
                data={},
                success=False
            )

        return api_response(
            status_code=201,
            message="Task assigned successfully",
            data=assigned_task,
            success=True
        )

    except Exception as e:

        print(f"Error occurred in assign_task route: {e}")

        return api_response(
            status_code=500,
            message="Internal server error",
            data={},
            success=False
        )


@router.get("/task-mappings")
def get_all_mappings(
    db: Session = Depends(get_db)
):

    try:

        mappings = user_task_services.get_all_task_mappings(db)

        return api_response(
            status_code=200,
            message="Mappings fetched successfully",
            data=mappings,
            success=True
        )

    except Exception as e:

        print(f"Error occurred in get_all_mappings route: {e}")

        return api_response(
            status_code=500,
            message="Internal server error",
            data={},
            success=False
        )


@router.get("/users/{user_id}/tasks")
def get_tasks_of_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    try:

        tasks = user_task_services.get_tasks_of_user(
            db,
            user_id
        )

        return api_response(
            status_code=200,
            message="User tasks fetched successfully",
            data=tasks,
            success=True
        )

    except Exception as e:

        print(f"Error occurred in get_tasks_of_user route: {e}")

        return api_response(
            status_code=500,
            message="Internal server error",
            data={},
            success=False
        )


@router.delete("/task-mapping/{mapping_id}")
def delete_mapping(
    mapping_id: int,
    db: Session = Depends(get_db)
):

    try:

        deleted = user_task_services.delete_task_mapping(
            db,
            mapping_id
        )

        if not deleted:

            return api_response(
                status_code=404,
                message="Mapping not found",
                data={},
                success=False
            )

        return api_response(
            status_code=200,
            message="Mapping deleted successfully",
            data={},
            success=True
        )

    except Exception as e:

        print(f"Error occurred in delete_mapping route: {e}")

        return api_response(
            status_code=500,
            message="Internal server error",
            data={},
            success=False
        )