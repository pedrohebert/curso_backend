from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    TO_DO = "TO DO"
    PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"


class Task(BaseModel):
    title: str
    description: str | None = None
    status: Status = Status.TO_DO


class PublicTask(Task):
    id: int


class UpdateTask(BaseModel):
    title: str | None
    description: str | None
    status: Status | None
