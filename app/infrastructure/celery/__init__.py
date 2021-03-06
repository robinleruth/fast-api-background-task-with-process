from celery import Celery

from . import celery_config
from app.infrastructure.config import app_config


celery = Celery(__name__, broker=app_config.CELERY_BROKER, backend=app_config.CELERY_BACKEND)
celery.config_from_object(celery_config)
celery.conf.update(app_config.__dict__)


from app.interface.web.celery_task.some_celery_task import some_celery_task
from app.domain.services.dispatch_service import async_task
# celery.register_task(DispatchService())
