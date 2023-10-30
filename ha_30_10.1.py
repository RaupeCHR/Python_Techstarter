products = [
    ("Laptop", 899.99, 4.6, True),
    ("Smartphone", 549.99, 4.2, True),
    ("Tablet", 299.99, 3.9, False),
    ("Kopfhörer", 149.99, 4.8, True),
    ("Maus", 19.99, 4.1, True),
]
# Aufgabe 1.1 "availible products"
availible_product = [product[0] for product in products if product[3] == True]

print(availible_product)

# Aufgabe 1.2
product_lower_than_50 = [product[0] for product in products if product[1] <= 50 and product[2] >= 4]

print(product_lower_than_50)

# Aufgabe 1.3
average_price = sum(product[1] for product in products) / len(products)

print(average_price)

# Aufgabe 1.4
highest_price = max(products, key=lambda x: x[1])

print(highest_price)