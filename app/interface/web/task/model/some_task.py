import time

from app.interface.web.task.model.task import Task
from app.domain.services.factory import service_factory


class SomeTask(Task):
    def __init__(self, tid, queue_log):
        super().__init__(tid, queue_log)
        self.service = service_factory()

    def run(self):
        self._log('info', 'sleep_for_2')
        self.service.sleep_for_2()
        self._log('info', f'update_smth_from_db')
        self.service.update_smth_from_db("a")
        self._log('info', 'get_smth_from_db')
        result = self.service.get_smth_from_db()
        self._log('info', f'result : {result}')
        self._log('info', f'update_smth_from_db')
        self.service.update_smth_from_db("b")
        self._log('info', 'get_smth_from_db')
        result = self.service.get_smth_from_db()
        self._log('info', f'result : {result}')
        # self._log('info', 'sleep_for_5')
        # self.service.sleep_for_5()
        # self._log('info', 'sleep_for_3')
        # self.service.sleep_for_3()
        self.ttl = time.time()
        self.result = result
        self._log('info', 'Done', True)
