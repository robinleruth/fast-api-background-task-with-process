import unittest

from unittest.mock import MagicMock
from datetime import date

from app.infrastructure.db_connector.mock_db_connector import MockDBConnector
from app.domain.services.cache_service.cache_service import CacheService
from app.domain.services.cache_service.redis_cache_service import RedisCacheService
from app.domain.model.some_model import SomeModel


class TestCacheService(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_service(self):
        connector = MockDBConnector()
        connector.get_by_date = MagicMock(return_value=[SomeModel(a=1, b='a')])
        self.service = CacheService(connector)
        lst = self.service.get_by_date(date(2020, 3, 30))
        print(lst)

    def test_redis_service(self):
        connector = MockDBConnector()
        connector.get_by_date = MagicMock(return_value=[SomeModel(a=1, b='a')])
        self.service = RedisCacheService(connector)
        lst = self.service.get_by_date(date(2020, 3, 30))
        print(lst)


if __name__ == '__main__':
    unittest.main(verbosity=2)
