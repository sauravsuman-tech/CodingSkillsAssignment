class Order:
    def __init__(self, user, products: list):
        self.id = self._generate_order_id()
        self.user = user
        self.products = products
        self.status = 'pending'
        self.payment = None

    def _generate_order_id(self):
        import random
        return random.randint(1000, 9999)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def complete_order(self, payment):
        self.status = 'completed'
        self.payment = payment

    def __repr__(self):
        return f"Order(id={self.id}, status={self.status}, products={self.products})"
