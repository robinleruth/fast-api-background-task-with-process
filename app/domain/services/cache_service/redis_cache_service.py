import redis
import pickle

from dataclasses import dataclass

from app.domain.services.cache_service.cache_service import CacheService


@dataclass
class RedisCacheService(CacheService):
    def __post_init__(self):
        super().__post_init__()
        self.models_by_date = redis.Redis()

    def _get_from_connector(self, key):
        return pickle.dumps(self.connector.get_by_date(key))

    def _get_from_dict(self, key):
        return pickle.loads(self.models_by_date[key])
