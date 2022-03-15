import unittest

from app.cashier.Cashier import Cashier
from app.cashier.Item import Item


class Requirement3Tests(unittest.TestCase):

    def test_should_cancel_item(self):
        cashier = Cashier()
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        self.assertEqual(1, cashier.basket_size())
        cashier.cancel(apple)
        self.assertEqual(0, cashier.basket_size())
