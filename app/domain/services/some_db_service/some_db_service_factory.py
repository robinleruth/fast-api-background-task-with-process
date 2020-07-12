from functools import lru_cache

from app.domain.services.some_db_service.some_db_service import SomeDbService


@lru_cache()
def some_db_service_factory() -> SomeDbService:
    return SomeDbService()
