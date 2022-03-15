import unittest

from app.cashier.Cashier import Cashier
from app.cashier.Item import Item


class Requirement1Tests(unittest.TestCase):

    def test_scan_single_item(self):
        cashier = Cashier()
        apple = Item("Apple", 1.0)
        self.assertEqual(1.0, apple.price)
        self.assertEqual("Apple", apple.name)
        cashier.scan(apple)
        self.assertEqual(1, cashier.basket_size())

    def test_scan_multiple_same_item(self):
        cashier = Cashier()
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        cashier.scan(apple)
        self.assertEqual(2, cashier.basket_size())

    def test_get_total(self):
        cashier = Cashier()
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        cashier.scan(apple)
        self.assertEqual(2.14, cashier.get_total())

    def test_scan_different_items(self):
        cashier = Cashier()
        cashier.gst = 0.0
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        cola = Item("Cola (1L)", 2.0)
        cashier.scan(cola)
        self.assertEqual(2, cashier.basket_size())
        self.assertEqual(3.0, cashier.get_total())

    def test_scan_bulk_items(self):
        cashier = Cashier()
        cashier.gst = 0.0
        apple = Item("Apple", 1.0)
        cashier.scan(apple, 2)
        cola = Item("Cola (1L)", 2.0)
        cashier.scan(cola)
        self.assertEqual(3, cashier.basket_size())
        self.assertEqual(4.0, cashier.get_total())

