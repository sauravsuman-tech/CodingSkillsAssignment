from Product import Product
from User import User
from Payment import Payment      

product1 = Product(1, "Laptop", 999.99)
product2 = Product(2, "Headphones", 199.99)
product3 = Product(3, "Mouse", 29.99)

user = User(1, "Saurav Kumar", "saurav@example.com", "123 Street, City")

order = user.create_order([product1, product2])

order.add_product(product3)

payment = Payment(order, sum([p.price for p in order.products]))
order.complete_order(payment)

print(order)
print(payment)

"""
Output : 

Order(id=6149, status=completed, products=[Product(id=1, name=Laptop, price=999.99), Product(id=2, name=Headphones, price=199.99), Product(id=3, name=Mouse, price=29.99)])
Payment(id=96552, order_id=6149, amount=1229.97, status=successful, date=2024-10-18 13:22:20.952000)

"""