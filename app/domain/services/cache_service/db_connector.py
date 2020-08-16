from abc import ABCMeta
from abc import abstractmethod
from typing import List

from app.domain.model.some_model import SomeModel


class DbConnector(metaclass=ABCMeta):
    @abstractmethod
    def get_by_date(self, date: str) -> List[SomeModel]:
        pass

