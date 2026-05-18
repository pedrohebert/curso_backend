from pydantic import BaseModel
from enum import Enum

class Status(Enum):
    TO_DO = "TO DO"
    PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"


class Task(BaseModel):
    title: str
    description: str
    status: Status


class PublicTask(Task):
    id: int


class UpdateTask(BaseModel):
    title: str | None
    description: str | None
    status: Status | None
