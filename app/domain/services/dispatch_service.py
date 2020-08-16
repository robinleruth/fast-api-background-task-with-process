from typing import List

from app.domain.model.client import Client
from app.domain.model.client import Output


class DispatchService:
    def process_client(self, client: Client) -> Output:
        return Output(name=client.name,
                      number_of_trades=len(client.trades))

    def process_clients(self, clients: List[Client]) -> List[Output]:
        return [self.process_client(client) for client in clients]
