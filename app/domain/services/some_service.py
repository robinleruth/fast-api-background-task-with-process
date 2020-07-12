import time

from dataclasses import dataclass

from app.domain.services.abstract_service import AbstractService
from app.domain.services.some_db_service.some_db_service_factory import some_db_service_factory


class SomeService(AbstractService):
    def get_smth_from_db(self) -> str:
        db_service = some_db_service_factory()
        return db_service.get_info_from_table(1)

    def update_smth_from_db(self, info):
        db_service = some_db_service_factory()
        db_service.update(1, info)

    def sleep_for_2(self):
        time.sleep(2)

    def sleep_for_3(self):
        time.sleep(3)

    def sleep_for_5(self):
        time.sleep(5)
