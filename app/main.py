from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.db.db import DB
from app.models.TaskModel import PublicTask, Task, UpdateTask

app = FastAPI()


db: DB = DB()


@app.post("/", status_code=201)
async def create_task(new_task: Task) -> PublicTask:
    task_id = db.create(new_task)
    return PublicTask(**new_task.model_dump(), id=task_id)


@app.get("/", status_code=200)
async def get_all_task() -> list[PublicTask]:
    return [PublicTask(**v.model_dump(), id=k) for k, v in db.get_all().items()]


@app.get("/{task_id}", status_code=200)
async def get_by_id(task_id: int) -> PublicTask:
    task_db = db.get(task_id)
    if task_db:
        return PublicTask(**task_db.model_dump(), id=task_id)
    raise HTTPException(status_code=404, detail="task not fould")


@app.patch("/")
async def update_task(task_id: int, task_update: UpdateTask) -> PublicTask:
    task_db = db.update(task_id, task_update)
    if task_db:
        return PublicTask(**task_db.model_dump(), id=task_id)
    raise HTTPException(status_code=404, detail="task not fould")


@app.delete("/{task_id}")
async def delete_task(task_id: int) -> PublicTask:
    task_deleted = db.delete(task_id)
    if task_deleted:
        return PublicTask(**task_deleted.model_dump(), id=task_id)
    raise HTTPException(status_code=404, detail="task not fould")
