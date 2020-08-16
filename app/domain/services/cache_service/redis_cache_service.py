import redis
import pickle
from typing import Set

from dataclasses import dataclass
from dataclasses import field

from app.domain.services.cache_service.cache_service import CacheService


@dataclass
class RedisCacheService(CacheService):
    keys: Set[str] = field(default_factory=set)

    def __post_init__(self):
        super().__post_init__()
        self.models_by_date = redis.Redis()

    def _get_from_connector(self, key):
        return pickle.dumps(self.connector.get_by_date(key))

    def _get_from_dict(self, key):
        if key not in self.keys:
            self.keys.add(key)
        return pickle.loads(self.models_by_date[key])

    def _refresh_cache(self):
        for d in self.keys:
            self.models_by_date[d] = self._get_from_connector(d)
