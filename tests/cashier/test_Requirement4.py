import unittest

from app.cashier.Cashier import Cashier
from app.cashier.DiscountRule import DiscountRule
from app.cashier.Item import Item


class Requirement4Tests(unittest.TestCase):

    def test_should_apply_discount(self):
        cashier = Cashier()
        cashier.gst = 0.0
        apple_discount_rule = DiscountRule(item_name="Apple", discount_percent=0.5)
        cashier.add_item_rule(apple_discount_rule)
        apple = Item("Apple", 1.0)
        cashier.scan(apple)
        cashier.finalise()
        self.assertEqual(0.5, cashier.get_total())

    def test_should_not_apply_discount(self):
        cashier = Cashier()
        cashier.gst = 0.0
        apple_discount_rule = DiscountRule(item_name="Apple", discount_percent=0.5)
        cashier.add_item_rule(apple_discount_rule)
        cola = Item("Cola", 1.0)
        cashier.scan(cola)
        cashier.finalise()
        self.assertEqual(1.0, cashier.get_total())

    def test_should_apply_discount_multiple(self):
        cashier = Cashier()
        cashier.gst = 0.0
        apple_discount_rule = DiscountRule(item_name="Apple", discount_percent=0.5)
        cola_discount_rule = DiscountRule(item_name="Cola", discount_percent=0.1)
        cashier.add_item_rule(apple_discount_rule)
        cashier.add_item_rule(cola_discount_rule)
        apple = Item("Apple", 1.0)
        cola = Item("Cola", 1.0)
        cashier.scan(apple)
        cashier.scan(cola)
        cashier.finalise()
        self.assertEqual(0.5 + 0.9, cashier.get_total())
