import time

from typing import List
from celery import Task

from app.domain.model.client import Client
from app.domain.model.client import Output
from app.infrastructure.celery import celery


class DispatchService:
    def process_client(self, client: Client) -> Output:
        return async_task(client)

    def process_clients(self, clients: List[Client]) -> List[Output]:
        res = async_task.chunks(zip(clients), 2).group().apply_async(queue='high_priority')
        res = res.get()
        flattened = [val for sublist in res for val in sublist]
        return flattened

    def process_clients_sync(self, clients: List[Client]) -> List[Output]:
        res = async_task.chunks(zip(clients), 10).apply_async(queue='high_priority')
        res = res.get()
        flattened = [val for sublist in res for val in sublist]
        return flattened

@celery.task()
def async_task(client: Client) -> Output:
    time.sleep(1)
    return Output(name=client.name, number_of_trades=len(client.trades))
