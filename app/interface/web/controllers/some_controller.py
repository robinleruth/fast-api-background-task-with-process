from fastapi import APIRouter
from fastapi import BackgroundTasks
from typing import List

from app.infrastructure.log import logger
from app.interface.web.task.task_service_factory import task_service_factory
from app.domain.services.some_service import SomeService


router = APIRouter()


@router.post('/', status_code=202)
async def some_post():
    logger.info('Starting service in background')
    task_service = task_service_factory()
    _id = task_service.start(SomeService.__name__)
    return _id


@router.get('/getUpdate', status_code=206)
async def get_update(_id):
    logger.info(f'Getting update for {_id}')
    task_service = task_service_factory()
    lst: List = task_service.get_update(_id)
    if len(lst) == 0:
        response = ""
    else:
        response = '\n'.join(lst)
    return response


@router.get('/getResult')
async def get_result(_id):
    logger.info(f'Getting result for {_id}')
    task_service = task_service_factory()
    response = task_service.get_result(_id)
    if response is None:
        return "Result not available yet"
    return response
