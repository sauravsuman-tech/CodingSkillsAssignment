from Items import Items

products_stock = {1: 50, 2: 30, 3: 5}
orders = [(1, 10), (2, 5), (3, 2)]  

item=Items()
restock_list =item.process_orders(products_stock, orders)

restocked_products = item.restock_items(products_stock, restock_list)

print(products_stock)

"""
Output : {1: 40, 2: 25, 3: 10}

"""