import time

from dataclasses import dataclass

from app.domain.services.abstract_service import AbstractService


class SomeService(AbstractService):
    def sleep_for_2(self):
        time.sleep(2)

    def sleep_for_3(self):
        time.sleep(3)

    def sleep_for_5(self):
        time.sleep(5)
