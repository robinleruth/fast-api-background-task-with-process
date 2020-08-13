from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends
from typing import List

from app.infrastructure.log import logger
from app.interface.web.task.task_service_factory import task_service_factory
from app.interface.web.task.task_service import TaskService
from app.domain.services.some_service import SomeService


router = APIRouter()


@router.post('/', status_code=202)
async def some_post(task_service: TaskService = Depends(task_service_factory)):
    logger.info('Starting service in background')
    _id = task_service.start(SomeService.__name__)
    return _id


@router.get('/getUpdate', status_code=206)
async def get_update(_id, task_service: TaskService = Depends(task_service_factory)):
    logger.info(f'Getting update for {_id}')
    response: List = task_service.get_update(_id)
    return response


@router.get('/getResult')
async def get_result(_id, task_service: TaskService = Depends(task_service_factory)):
    logger.info(f'Getting result for {_id}')
    response = task_service.get_result(_id)
    if response is None:
        return "Result not available yet"
    return response
