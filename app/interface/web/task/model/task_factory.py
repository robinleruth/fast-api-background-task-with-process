from app.interface.web.task.model.task import Task
from app.interface.web.task.model.some_task import SomeTask
from app.domain.services.some_service import SomeService


def task_factory(service_name: str) -> Task:
    if service_name == SomeService.__name__:
        return SomeTask
    raise TaskNotFoundException(f'{service_name} not in task_factory !')
