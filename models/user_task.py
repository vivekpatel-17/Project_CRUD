from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)

from datetime import datetime, timezone

from core.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class UserTaskMapping(Base):

    __tablename__ = "user_task_mapping"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    task_id = Column(
        Integer,
        ForeignKey("tasks.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        default=utc_now
    )