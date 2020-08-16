from celery.utils.log import get_task_logger

from app.infrastructure.celery import celery
from app.domain.services.factory import service_factory

logger = get_task_logger(__name__)


@celery.task(bind=True)
def some_celery_task(self, first_arg):
    audit_trails = []
    print(first_arg)
    def _log(message):
        logger.info(message)
        audit_trails.append(message)
        self.update_state(state='PROGRESS', meta={'status': '\n'.join(audit_trails)})
    service: SomeService = service_factory()
    logger.info('sleep_for_2')
    audit_trails.append('sleep_for_2')
    self.update_state(state='PROGRESS', meta={
        # current, total, if we want a percentage, or just a "progress" variable
        'status': 'sleep_for_2'
    })
    service.sleep_for_2()
    _log(f'update_smth_from_db')
    service.update_smth_from_db("a")
    result = service.get_smth_from_db()
    _log(f'result : {result}')
    _log(f'update_smth_from_db')
    service.update_smth_from_db("b")
    _log('get_smth_from_db')
    result = service.get_smth_from_db()
    _log('sleep_for_2')
    service.sleep_for_2()
    _log(f'result : {result}')
    _log('Done!')
    return result
