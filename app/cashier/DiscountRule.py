from cashier.Item import Item
from cashier.ItemRule import ItemRule


class DiscountRule(ItemRule):

    def __init__(self, item_name: str, discount_percent: float = 0.0):
        super().__init__()
        self.item_name = item_name
        self.discount_percent = discount_percent

    def apply_to_item(self, item: Item):
        item.price = item.price - (item.price * self.discount_percent)

    def can_be_applied_to_item(self, item):
        can = self.item_name == item.name
        return can
