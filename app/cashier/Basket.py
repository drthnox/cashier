from cashier import BasketRule


class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

    def remove(self, item):
        for _i in self.items:
            if _i.__eq__(item):
                self.items.remove(item)

    def contains(self, item):
        for _i in self.items:
            if _i.__eq__(item):
                return True
        return False

    def apply_rule(self, rule):
        if isinstance(rule, BasketRule.BasketRule):
            rule.apply_to_basket(self)

    def get_total(self):
        total = 0.0
        for i in self.items:
            total += i.price
        return total
