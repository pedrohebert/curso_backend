from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.db.db import DB
from app.models.TaskModel import PublicTask, Task, UpdateTask

app = FastAPI()


db: DB = DB()


@app.post("/", status_code=201)
async def create_task(new_task: Task) -> PublicTask:
    saved_task_id = db.create(new_task)
    saved_task = db.get(saved_task_id)
    print(saved_task)
    assert saved_task is not None
    return PublicTask.model_validate(saved_task.model_dump())


@app.get("/all", status_code=200)
async def get_all_task() -> list[PublicTask]:
    return [PublicTask.model_validate(v.model_dump()) for v in db.get_all()]


@app.get("/{task_id}", status_code=200)
async def get_by_id(task_id: str) -> PublicTask:
    task_db = db.get(task_id)
    if task_db:
        return PublicTask.model_validate(task_db.model_dump())
    raise HTTPException(status_code=404, detail="task not fould")


@app.get("/")
async def get_filtred(
    title: str | None = None, description: str | None = None, status: str | None = None
) -> list[PublicTask]:
    return [
        PublicTask.model_validate(task.model_dump())
        for task in db.get_filtred(title, description, status)
    ]


@app.patch("/")
async def update_task(task_id: str, task_update: UpdateTask) -> PublicTask:
    db.update(task_id, task_update)
    task_db = db.get(task_id)
    if task_db:
        return PublicTask.model_validate(task_db.model_dump())
    raise HTTPException(status_code=404, detail="task not fould")


@app.delete("/{task_id}")
async def delete_task(task_id: str) -> PublicTask:
    task_deleted = db.delete(task_id)
    if task_deleted:
        return PublicTask.model_validate(task_deleted.model_dump())
    raise HTTPException(status_code=404, detail="task not fould")
