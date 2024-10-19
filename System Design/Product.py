class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"
