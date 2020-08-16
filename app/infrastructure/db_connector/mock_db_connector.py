import random

from typing import List

from app.domain.services.cache_service.db_connector import DbConnector
from app.domain.model.some_model import SomeModel


class MockDBConnector(DbConnector):
    lst = ['a', 'b', 'c' ,'d']

    def get_by_date(self, date: str) -> List[SomeModel]:
        return [SomeModel(a=random.randint(1, 5), b=random.choice(lst)) for _ in range(random.randint(1, 5))]
