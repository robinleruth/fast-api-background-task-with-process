from functools import lru_cache

from app.domain.services.cache_service.cache_service import CacheService
from app.infrastructure.db_connector.mock_db_connector import MockDBConnector


@lru_cache
def get_cache_service() -> CacheService:
    connector = MockDBConnector()
    return CacheService(connector)
