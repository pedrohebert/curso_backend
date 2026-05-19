from app.models.TaskModel import Task, UpdateTask


def id_gen():
    id = 0
    while True:
        yield id
        id += 1


class DB:
    __db: dict[int, Task] = {}
    __id = id_gen()

    def get_new_id(self) -> int:
        return next(self.__id)

    def create(self, new_task: Task, /) -> int:
        new_id = self.get_new_id()
        self.__db[new_id] = new_task
        return new_id

    def get_all(self) -> dict[int, Task]:
        return self.__db

    def get(self, task_id: int, /) -> Task | None:
        return self.__db.get(task_id)

    def get_filtred(
        self,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None,
    ):
        return {
            id: task
            for id, task in self.get_all().items()
            if (
                (title is None or title in task.title)
                and (
                    description is None
                    or (
                        task.description is not None and description in task.description
                    )
                )
                and (status is None or status in task.status.value)
            )
        }

    def delete(self, task_id: int, /) -> Task | None:
        return self.__db.pop(task_id)

    def update(self, task_id: int, update_task: UpdateTask, /) -> Task | None:
        task_db = self.get(task_id)
        if task_db:
            task_db.model_copy(update=update_task.model_dump(exclude_none=True))

        return task_db
