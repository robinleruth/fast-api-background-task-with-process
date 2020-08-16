from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from celery import states

from app.infrastructure.log import logger
from app.infrastructure.celery import celery
from app.domain.services.factory import service_factory
from app.interface.web.celery_task.some_celery_task import some_celery_task


router = APIRouter()


@router.post('/', status_code=202)
async def some_post():
    logger.info('Starting service in background')
    task = some_celery_task.apply_async(args=('first_args', ), countdown=2) # queue = '', countodnw=10 -> executed at the earliest 10 seconds after
    return task.id


@router.get('/getUpdate', status_code=206)
async def get_update_or_result(_id, response: Response):
    task = some_celery_task.AsyncResult(_id)
    if task.state == states.PENDING:
        raise HTTPException(status_code=404, detail="Task still pending, awaiting a worker to be processed")
    if task.state == 'PROGRESS':
        response = {
            'state': task.state,
            'status': task.info.get('status', '')
        }
        return response
    if task.state == 'FAILURE':
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return task.info
    response.status_code = status.HTTP_200_OK
    result = task.get()
    return result # propagate = False if i don't want the errors to propagate
# res.failed() and res.successful() gives True or False
# PENDING -> STARTED -> SUCCESS
