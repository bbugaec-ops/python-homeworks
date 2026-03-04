class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def display(self) -> str:
        return f"{self.name} — {self.price:.2f} грн"


products = [
    Product("Keyboard", 500),
    Product("Mouse", 300),
    Product("Monitor", 7000),
]

for p in products:
    print(p.display())
