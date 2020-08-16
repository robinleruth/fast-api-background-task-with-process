from typing import List
from celery import Task

from app.domain.model.client import Client
from app.domain.model.client import Output
from app.infrastructure.celery import celery


class DispatchService(Task):
    name = 'app.domain.services.dispatch_service.DispatchService'

    def run(self, client: Client) -> Output:
        return self.process_client(client)

    def process_client(self, client: Client) -> Output:
        return Output(name=client.name,
                      number_of_trades=len(client.trades))

    def process_clients(self, clients: List[Client]) -> List[Output]:
        res = self.chunks(clients, 2).apply_async(queue='high_priority')
        return res.get()

# DispatchService = celery.register_task(DispatchService())
