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


@dataclass
class CacheService:
    connector: DbConnector
    models_by_date: Dict[str, List[SomeModel]] = field(default_factory=dict)
    # IntVar boolean Redis is possible ? use redis : use dict
    # create Cache service as a bean

    def __post_init__(self):
        if app_config is not TestConfig:
            Thread(target=self.refresh).start()

    def get_by_date(self, date: date) -> List[SomeModel]:
        key = date.strftime('%Y-%m-%d')
        if key not in self.models_by_date:
            self.models_by_date[key] = self.connector.get_by_date(key)
        return self.models_by_date[key]

    def refresh(self):
        while True:
            for d in self.models_by_date:
                self.models_by_date[d] = self.connector.get_by_date(key)
            time.sleep(60)
