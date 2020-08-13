from fastapi import APIRouter

from app.infrastructure.log import logger


router = APIRouter()


@router.post('/', status_code=202)
async def some_post():
    logger.info('Starting service in background')
    return 1


@router.get('/getUpdate', status_code=206)
async def get_update(_id):
    logger.info(f'Getting update for {_id}')
    return 1


@router.get('/getResult')
async def get_result(_id):
    logger.info(f'Getting result for {_id}')
    return "Result not available yet"
