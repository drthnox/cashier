import unittest

from cashier.DiscountRule import DiscountRule
from cashier.Item import Item


class DiscountRuleTest(unittest.TestCase):

    def test_should_apply_rule(self):
        rule = DiscountRule("Apple", 0.5)
        apple = Item("Apple", 1.0)
        apple.apply_rule(rule)
        self.assertEqual(0.5, apple.price)

    def test_should_not_apply_rule(self):
        rule = DiscountRule("Apple", 0.5)
        cola = Item("Cola", 1.0)
        cola.apply_rule(rule)
        self.assertEqual(1.0, cola.price)
