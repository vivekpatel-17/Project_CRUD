from pydantic import BaseModel
from datetime import datetime


class UserTaskCreate(BaseModel):

    user_id: int

    task_id: int


class UserTaskResponse(BaseModel):

    id: int

    user_id: int

    task_id: int

    created_at: datetime

    class Config:
        from_attributes = True