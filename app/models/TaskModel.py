from pydantic import BaseModel
from enum import Enum

from pydantic.fields import Field

class Status(str, Enum):
    TO_DO = "TO DO"
    PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"


class Task(BaseModel):
    title: str
    description: str | None = None
    status: Status = Field(default= Status.TO_DO)


class PublicTask(Task):
    id: str

class DBTask(Task):
    id:str = Field(alias="_id")


class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    status: Status | None = None
