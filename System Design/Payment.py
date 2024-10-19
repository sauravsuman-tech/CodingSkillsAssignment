from Order import Order
class Payment:
    def __init__(self, order: Order, amount: float):
        self.id = self._generate_payment_id()
        self.order = order
        self.amount = amount
        self.status = 'successful'
        self.date = self._current_date()

    def _generate_payment_id(self):
        import random
        return random.randint(10000, 99999)

    def _current_date(self):
        from datetime import datetime
        return datetime.now()

    def __repr__(self):
        return f"Payment(id={self.id}, order_id={self.order.id}, amount={self.amount}, status={self.status}, date={self.date})"
