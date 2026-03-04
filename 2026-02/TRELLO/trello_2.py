class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


products = [
    Product("Піца",249),
    Product("Кава", 50),
    Product("Чай", 40),
    Product("Тістечко", 70)
]

for product in products:
    print(f"{product.name} — {product.price} грн")
