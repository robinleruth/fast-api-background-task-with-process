from typing import List
from celery import Task

from app.domain.model.client import Client
from app.domain.model.client import Output
from app.infrastructure.celery import celery


class DispatchService:
    def process_client(self, client: Client) -> Output:
        return async_task(client)

    def process_clients(self, clients: List[Client]) -> List[Output]:
        res = async_task.chunks(iter(clients), 10).group().apply_async()#queue='high_priority')
        return res.get()

@celery.task()
def async_task(client: Client) -> Output:
    return Output(name=client.name, number_of_trades=len(client.trades))
