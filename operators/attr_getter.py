from operator import attrgetter


class Order:
    def __init__(self, order_id):
        self.order_id = order_id

    def __repr__(self):
        return f"Order({self.order_id})"


orders = [Order(23), Order(6), Order(15), Order(11)]

print(sorted(orders, key=attrgetter("order_id")))
