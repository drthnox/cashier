import uuid

from app.cashier.Basket import Basket


class Cashier:

    def __init__(self):
        self.basket = Basket()
        self.total = 0.0
        self.item_rules = []
        self.basket_rules = []
        self.gst = 0.07
        self.sub_total = 0.0

    def scan(self, item, number=1):
        for _ in range(number):
            item.id = uuid.uuid1()
            self.basket.add(item)

    def basket_size(self):
        return self.basket.count()

    def get_subtotal(self):
        # basket total is total before application of gst
        return self.basket.get_total()

    def get_total(self):
        return self.get_subtotal() * float(1.0 + self.gst)

    def print_receipt(self):
        receipt = ''
        for item in self.basket.items:
            receipt += item.name
            receipt += ':'
            receipt += str(item.price)
            receipt += '\n'
        receipt += 'Sub-Total:'
        receipt += str(self.get_subtotal())
        receipt += '\nTotal:'
        receipt += str(self.get_total())
        return receipt

    def add_item_rule(self, rule):
        self.item_rules.append(rule)

    def add_basket_rule(self, rule):
        self.basket_rules.append(rule)

    def finalise(self):
        self.apply_item_rules()
        self.apply_basket_rules()

    def apply_item_rules(self):
        for rule in self.item_rules:
            for item in self.basket.items:
                if rule.can_be_applied_to_item(item):
                    rule.apply_to_item(item)

    def apply_basket_rules(self):
        for rule in self.basket_rules:
            self.basket.apply_rule(rule)

    def cancel(self, item):
        self.basket.remove(item)
