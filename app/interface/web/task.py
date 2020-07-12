import time
import multiprocessing as mp

from typing import Dict, Any

from app.domain.services.some_service import SomeService
from app.domain.services.factory import service_factory


class Task(mp.Process):
    tid: str
    queue_log: mp.Queue
    queue: mp.Queue
    ttl: int = None
    service: SomeService # or provided by TaskService
    # if not provided by TaskService, Task might actually be an abstract class
    # and run() has to polymorphism for each Service !
    result: Any = None

    def __init__(self, tid, queue_log):
        super().__init__()
        self.tid = tid
        self.queue_log = queue_log
        self.queue = mp.Queue()
        self.service = service_factory()

    def run(self):
        self._log('info', 'sleep_for_2')
        self.service.sleep_for_2()
        self._log('info', 'sleep_for_5')
        self.service.sleep_for_5()
        self._log('info', 'sleep_for_3')
        self.service.sleep_for_3()
        self.ttl = time.time()
        self.result = 'Done !'
        self._log('info', 'Done', True)

    def _log(self, level, message, done=False):
        msg = {
            'level': level,
            'message': f'{self.tid} : {message}'
        }
        if done:
            msg['ttl'] = self.ttl
            msg['result'] = self.result
            msg['tid'] = self.tid
        self.queue.put(f'{self.tid} : {message}')
        self.queue_log.put(msg)

    def is_dead_for_more_than_5_minutes(self) -> bool:
        five_min_ago = int(time.time()) - 5 * 60
        if self.ttl is not None and self.ttl > five_min_ago:
            return True
        else:
            return False

    @property
    def serialize(self):
        return  {
            'tid': self.tid,
            'ttl':  str(self.ttl) or 'None',
            'result':  self.result or 'None',
            'is_dead_for_more_than_5_minutes': self.is_dead_for_more_than_5_minutes()
        }
