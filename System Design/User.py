from Order import Order
class User:
    def __init__(self, user_id: int, name: str, email: str, address: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.orders = []

    def create_order(self, products):
        order = Order(self, products)
        self.orders.append(order)
        return order

    def view_orders(self):
        return self.orders
  