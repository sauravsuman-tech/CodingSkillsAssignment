class Items:
    def process_orders(self,products_stock: dict, orders: list, threshold: int = 10):
        """
        Process incoming orders and reduce stock levels. Trigger restocking if needed.

        :param products_stock: Dictionary of products with their current stock levels.
        :param orders: List of tuples representing orders. Each tuple contains (product_id, quantity).
        :param threshold: The stock level below which restocking is triggered.
        :return: List of products that need restocking.
        """
        restock_needed = []

        for product_id, quantity in orders:
            if product_id not in products_stock:
                raise ValueError(f"Product {product_id} does not exist in the stock.")

            if products_stock[product_id] < quantity:
                raise ValueError(f"Not enough stock for product {product_id}.")

            products_stock[product_id] -= quantity

            if products_stock[product_id] < threshold:
                restock_needed.append((product_id, threshold - products_stock[product_id]))

        return restock_needed
    def restock_items(self,products_stock: dict, restock_orders: list):
        """
        Restock items by updating the stock levels.

        :param products_stock: Dictionary of products with their current stock levels.
        :param restock_orders: List of tuples representing restock orders. Each tuple contains (product_id, quantity).
        """
        for product_id, quantity in restock_orders:
            if product_id not in products_stock:
                raise ValueError(f"Product {product_id} does not exist in the stock.")

            products_stock[product_id] += quantity

        return products_stock
