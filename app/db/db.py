from bson import ObjectId

from app.models.TaskModel import DBTask, Task, UpdateTask
from pymongo import MongoClient

def id_gen():
    id = 0
    while True:
        yield id
        id += 1

URI= "mongodb://root:12345@localhost:27017"
client = MongoClient(URI)
db=client["minha_api"]
collection = db['tesks']

class DB:
    __db: dict[int, Task] = {}
    __id = id_gen()


    def create(self, new_task: Task, /) -> str:
        result = collection.insert_one(new_task.model_dump())
        return str(result.inserted_id)

    def get_all(self) -> list[DBTask]:
        tasks: list[DBTask] = []

        for t in collection.find():
            t["_id"] = str(t["_id"])
            tasks.append(DBTask.model_validate(t))
        return tasks

    def get(self, task_id: str, /) -> DBTask | None:
        db_task = collection.find_one({"_id": ObjectId(task_id)})
        if db_task is not None:
            db_task["_id"] =  str(db_task["_id"])
            db_task = DBTask.model_validate(db_task)
        return db_task

    def get_filtred(
        self,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None,
    ) -> list[DBTask]:
        return []

    def delete(self, task_id: str, /) -> DBTask | None:
        db_task = collection.find_one_and_delete({"_id": ObjectId(task_id)})
        if db_task is not None:
            db_task["_id"] =  str(db_task["_id"])
            db_task = DBTask.model_validate(db_task)
        return db_task

    def update(self, task_id: str, update_task: UpdateTask, /) -> None:
        collection.update({"_id": ObjectId(task_id)}, {"$set":update_task.model_dump(exclude_none=True, exclude_unset=True)})
