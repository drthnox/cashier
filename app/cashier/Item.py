from cashier.Rule import Rule


class Item:

    def __init__(self, name, price=0.0):
        self.name = name
        self.price = price
        self.id = None

    def apply_rule(self, rule: Rule):
        if rule.can_be_applied_to_item(self):
            rule.apply_to_item(self)
