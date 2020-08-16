from fastapi import APIRouter
from fastapi import Depends
from typing import List

from app.domain.services.dispatch_service import DispatchService
from app.domain.model.client import Output
from app.domain.model.client import Client


router = APIRouter()


@router.post('/byClient', status_code=201, response_model=Output)
async def process_clients(client: Client,
                          service: DispatchService = Depends(DispatchService)):
    res = service.process_client(client)
    return res


@router.post('/byClients', status_code=201, response_model=List[Output])
async def process_clients(clients: List[Client],
                          service: DispatchService = Depends(DispatchService)):
    res = service.process_clients(clients)
    return res
