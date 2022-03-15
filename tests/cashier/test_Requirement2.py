import unittest

from app.cashier.Cashier import Cashier
from app.cashier.Item import Item


class Requirement2Tests(unittest.TestCase):

    def test_get_receipt(self):
        cashier = Cashier()
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        receipt = cashier.print_receipt()
        self.assertEqual("Apple:1.0\nSub-Total:1.0\nTotal:1.07", receipt)

    def test_get_receipt_multiple(self):
        cashier = Cashier()
        cashier.gst = 0.0
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        cola = Item("Cola", 2.0)
        cashier.scan(cola)
        receipt = cashier.print_receipt()
        self.assertEqual("Apple:1.0\nCola:2.0\nSub-Total:3.0\nTotal:3.0", receipt)
