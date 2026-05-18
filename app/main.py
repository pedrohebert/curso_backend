from enum import Enum
from typing import TypedDict

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()


class Status(Enum):
    TO_DO = "TO DO"
    PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"


class Task(TypedDict):
    title: str
    description: str
    status: Status


class PublicTask(Task):
    id: int


class UpdateTask(TypedDict, total=False):
    title: str | None
    description: str | None
    status: Status | None


db: dict[int, Task] = {}


def id_gen():
    id = 0
    while True:
        yield id
        id += 1


_id = id_gen()


def get_new_id() -> int:
    return next(_id)


@app.post("/", status_code=201)
async def create_task(task: Task) -> PublicTask:
    new_id = get_new_id()
    db[new_id] = task
    return PublicTask(**db[new_id], id=new_id)


@app.get("/all")
async def get_all_task() -> list[PublicTask]:
    return [PublicTask(**v, id=k) for k, v in db.items()]


@app.get("/{task_id}")
async def get_by_id(task_id: int) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")
    return PublicTask(**db[task_id], id=task_id)


@app.patch("/")
async def update_task(task_id: int, update: UpdateTask) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")

    up = list((k, v) for k, v in update.items() if v is not None)
    db[task_id].update(up)

    return PublicTask(**db[task_id], id=task_id)


@app.delete("/{task_id}")
async def delete_task(task_id: int) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")

    deleted = db.pop(task_id)
    return PublicTask(**deleted, id=task_id)
