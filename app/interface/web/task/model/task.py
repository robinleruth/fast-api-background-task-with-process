import time
import multiprocessing as mp

from abc import ABCMeta
from abc import abstractmethod

from typing import Dict, Any

from app.domain.services.factory import service_factory
from app.domain.services.abstract_service import AbstractService


class Task(mp.Process, metaclass=ABCMeta):
    tid: str
    queue_log: mp.Queue
    queue: mp.Queue
    ttl: int = None
    service: AbstractService
    result: Any = None

    def __init__(self, tid, queue_log):
        super().__init__()
        self.tid = tid
        self.queue_log = queue_log
        self.queue = mp.Queue()

    @abstractmethod
    def run(self):
        pass

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
        if self.ttl is not None and self.ttl < five_min_ago:
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
