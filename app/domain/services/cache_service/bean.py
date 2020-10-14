import redis

from functools import lru_cache

from app.domain.services.cache_service.cache_service import CacheService
from app.domain.services.cache_service.redis_cache_service import RedisCacheService
from app.infrastructure.db_connector.mock_db_connector import MockDBConnector
from app.infrastructure.log import logger


@lru_cache()
def get_cache_service() -> CacheService:
    connector = MockDBConnector()
    r = redis.Redis()
    try:
        r.ping()
        logger.info('Redis connection available')
        service = RedisCacheService(connector)
    except:
        service = CacheService(connector)
    return service
