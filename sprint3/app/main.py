from fastapi import FastAPI
from typing import Sequence, TypedDict

from fastapi.exceptions import HTTPException

app = FastAPI()


class Task(TypedDict):
    title: str
    description: str
    status: str

class PublicTask(Task):
    id:int

class UpdateTask(TypedDict, total=False):
    title: str | None
    description: str | None
    status: str | None


db:dict[int, Task] = {}


def id_gen():
    id = 0
    while True:
        yield id
        id += 1


_id = id_gen()


def get_new_id() -> int:
    return next(_id)


@app.post("/")
async def create_task(task: Task) -> PublicTask:
    id = get_new_id()
    db[id] = task
    return {**task, "id":id}

@app.get("/all")
async def get_all_task() -> list[PublicTask]:
    saida:list[PublicTask] = [{**v, "id":k} for k,v in db.items()]
    return saida

@app.get("/{task_id}")
async def get_by_id(task_id:int) -> PublicTask:
    if task_id not in db:
        raise HTTPException(status_code=404, detail="task not fould")
    return {**db[task_id], "id":task_id}

@app.put("/")
async def update_task(id:int,update: UpdateTask) -> PublicTask:
    if id not in db:
        raise HTTPException(status_code=404, detail="task not fould")

    up = list((k,v) for k,v in update.items() if v is not None)
    db[id].update(up)

    return {**db[id], "id":id}
