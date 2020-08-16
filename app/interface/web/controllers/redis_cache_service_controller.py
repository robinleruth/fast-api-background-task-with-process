from datetime import date
from fastapi import APIRouter
from fastapi import Depends

from app.domain.services.cache_service.cache_service import CacheService
from app.domain.services.cache_service.bean import get_cache_service


router = APIRouter()


@router.get('/')
async def get_model(date: date, service: CacheService = Depends(get_cache_service)):
    return service.get_by_date(date)
