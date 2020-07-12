from functools import lru_cache

from app.domain.services.some_service import SomeService


@lru_cache()
def service_factory():
    return SomeService()
