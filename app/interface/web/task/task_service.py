import time
import uuid
import threading
import multiprocessing as mp

from typing import Dict
from typing import List
from dataclasses import dataclass
from dataclasses import field

from app.infrastructure.log import logger
from app.interface.web.task.model.task_factory import task_factory
from app.interface.web.task.model.task import Task


@dataclass
class TaskService:
    tasks: Dict[str, Task] = field(default_factory=dict)
    queue_log: mp.Queue = field(default_factory=mp.Queue)

    def __post_init__(self):
        t = threading.Thread(target=self._log)
        t.daemon = True
        t.start()
        t = threading.Thread(target=self._clean_tasks)
        t.daemon = True
        t.start()

    def start(self, service_name: str):
        _id = uuid.uuid4().hex
        task_class = task_factory(service_name)
        t = task_class(tid=_id, queue_log=self.queue_log)
        t.daemon = True
        self.tasks[_id] = t
        t.start()
        return _id

    def get_update(self, _id) -> List:
        lst = []
        prefix = f'{_id} : '
        while not self.tasks[_id].queue.empty():
            res = self.tasks[_id].queue.get()
            lst.append(res.replace(prefix, ''))
        return lst

    def get_result(self, _id):
        return self.tasks[_id].result

    def _log(self):
        while True:
            msg = self.queue_log.get()
            if msg['level'] == 'info':
                logger.info(msg['message'])
            elif msg['level'] == 'error':
                logger.error(msg['message'])
            else:
                logger.debug(msg['message'])
            if msg.get('tid'):
                tid = msg['tid']
                self.tasks[tid].ttl = msg['ttl']
                self.tasks[tid].result = msg['result']

    def _clean_tasks(self):
        while True:
            self.tasks = {
                _id: task for _id, task in self.tasks.items()
                if not task.is_dead_for_more_than_5_minutes()
            }
            # time.sleep(60)
            time.sleep(60)
            logger.info(f'Keys : {[i for i in self.tasks.keys()]}')
