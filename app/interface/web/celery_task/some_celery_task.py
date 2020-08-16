from celery.utils.log import get_task_logger

from app.infrastructure.celery import celery
from app.domain.services.factory import service_factory

logger = get_task_logger(__name__)


@celery.task(bind=True)
def some_celery_task(self, first_arg):
    print(first_arg)
    service: SomeService = service_factory()
    logger.info('sleep_for_2')
    self.update_state(state='PROGRESS', meta={
        # current, total, if we want a percentage, or just a "progress" variable
        'status': 'sleep_for_2'
    })
    service.sleep_for_2()
    logger.info(f'update_smth_from_db')
    self.update_state(state='PROGRESS', meta={'status': 'update_smth_from_db'})
    service.update_smth_from_db("a")
    logger.info('get_smth_from_db')
    self.update_state(state='PROGRESS', meta={'status': 'get_smth_from_db'})
    result = service.get_smth_from_db()
    logger.info(f'result : {result}')
    self.update_state(state='PROGRESS', meta={'status': 'result : {result}'})
    logger.info(f'update_smth_from_db')
    self.update_state(state='PROGRESS', meta={'status': 'update_smth_from_db'})
    service.update_smth_from_db("b")
    logger.info('get_smth_from_db')
    self.update_state(state='PROGRESS', meta={'status': 'get_smth_from_db'})
    result = service.get_smth_from_db()
    logger.info(f'result : {result}')
    self.update_state(state='PROGRESS', meta={'status': 'result : {result}'})
    logger.info('Done', True)
    self.update_state(state='PROGRESS', meta={'status': 'Done'})
    return result
