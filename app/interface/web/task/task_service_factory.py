from functools import lru_cache

from app.interface.web.task.task_service import TaskService


@lru_cache(maxsize=1)
def task_service_factory():
    return TaskService()
