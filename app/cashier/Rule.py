class Rule(object):

    def __init__(self):
        pass

    def apply_to_item(self, item):
        pass

    def apply_to_basket(self, basket):
        pass

    def can_be_applied_to_item(self, item):
        return False

    def can_be_applied_to_basket(self, basket):
        return False
