from enum import Enum
from typing import TypedDict

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.models.TaskModel import Task, PublicTask, UpdateTask

app = FastAPI()


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
    return PublicTask(**task.model_dump(), id=new_id)


@app.get("/all")
async def get_all_task() -> list[PublicTask]:
    return [PublicTask(**v.model_dump(), id=k) for k, v in db.items()]


@app.get("/{task_id}")
async def get_by_id(task_id: int) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")
    return PublicTask(**db[task_id].model_dump(), id=task_id)


@app.patch("/")
async def update_task(task_id: int, update: UpdateTask) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")

    db_task = update.model_dump(exclude_none=True, exclude_unset=True)
    db[task_id].model_copy(update=db_task)
    return PublicTask(**db[task_id].model_dump(), id=task_id)


@app.delete("/{task_id}")
async def delete_task(task_id: int) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")

    deleted = db.pop(task_id)

    return PublicTask(**deleted.model_dump(), id=task_id)
