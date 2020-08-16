import time

from typing import List
from typing import Dict
from dataclasses import dataclass
from dataclasses import field
from datetime import date
from threading import Thread

from app.domain.services.cache_service.db_connector import DbConnector
from app.domain.model.some_model import SomeModel
from app.infrastructure.config import app_config
from app.infrastructure.config import TestConfig
from app.infrastructure.log import logger


@dataclass
class CacheService:
    connector: DbConnector
    models_by_date: Dict[str, List[SomeModel]] = field(default_factory=dict)
    # InitVar boolean Redis is possible ? use redis : use dict
    # create Cache service as a bean

    def __post_init__(self):
        logger.info('Init Cache Service')
        if app_config is not TestConfig:
            logger.info('Launch refresh every minute')
            Thread(target=self.refresh).start()

    def get_by_date(self, date: date) -> List[SomeModel]:
        key = date.strftime('%Y-%m-%d')
        if key not in self.models_by_date:
            self.models_by_date[key] = self._get_from_connector(key)
        return self._get_from_dict(key)

    def refresh(self):
        while True:
            self._refresh_cache()
            time.sleep(60)

    def _refresh_cache(self):
        for d in self.models_by_date:
            self.models_by_date[d] = self._get_from_connector(d)

    def _get_from_connector(self, key):
        return self.connector.get_by_date(key)

    def _get_from_dict(self, key):
        return self.models_by_date[key]
