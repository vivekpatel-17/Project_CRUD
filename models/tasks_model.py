from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Boolean
from datetime import datetime, timezone
from core.database import Base



def utc_now():
    return datetime.now(timezone.utc)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255) , nullable = False)
    description = Column(String(255))
    completed = Column(Boolean,default=False)
    created_at = Column(
        DateTime(timezone=True),
        default=utc_now
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now
    )
