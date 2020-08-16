import unittest

from app.domain.services.dispatch_service import DispatchService
from app.domain.model.client import Trade
from app.domain.model.client import Client
from app.domain.model.client import Output


class TestDispatchService(unittest.TestCase):
    def setUp(self):
        self.service = DispatchService()

    def tearDown(self):
        pass

    def test_process_single_client(self):
        c = Client(name="foo", trades=[Trade(ticker='AAPL', price=20.2),
                                       Trade(ticker='GOOG', price=20)])
        output: Output = self.service.process_client(c)
        self.assertEqual(2, output.number_of_trades)

    def test_process_multiple_clients(self):
        lst = []
        lst.append(Client(name="foo", trades=[Trade(ticker='AAPL', price=20.2), Trade(ticker='GOOG', price=20)]))
        lst.append(Client(name="aa", trades=[Trade(ticker='AAPL', price=20.2)]))
        res = self.service.process_clients(lst)
        self.assertEqual(2, res[0].number_of_trades)
        self.assertEqual(1, res[1].number_of_trades)


if __name__ == '__main__':
    unittest.main(verbosity=2)
