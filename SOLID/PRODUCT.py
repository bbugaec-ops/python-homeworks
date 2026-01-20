class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} грн"

class Order:
    def __init__(self,order_id):
        self.order_id = order_id
        self.items = []
        self.status = "Нове"

    def add_items(self,product,quantity):
        self.items.append({"product": product, "quantity": quantity})


    def calculate_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def update_status(self,new_status):
        self.status = new_status


    def __str__(self):
        details = "\n".join([f" - {i['product'].name} x {i['quantity']}" for i in self.items])
        return (f"Замовлення № {self.order_id}\nСтатус: {self.status}\n"
                f"Товари:\n {details}\nРазом до сплати: {self.calculate_total()} грн")


class OrderManager:
    def __init__(self):
        self.orders = {}

    def create_order(self,order_id):
        new_order = Order(order_id)
        self.orders[order_id] = new_order
        return new_order

    def get_order(self,order_id):
        return self.orders.get(order_id,"замовлення не знайдено")



laptop = Product("Ноутбук", 35000)
mause = Product("Мишка", 1200)

manager = OrderManager()

order101 = manager.create_order(101)
order101.add_items(laptop,1)
order101.add_items(mause,2)


order101.update_status("Сплачено")

print(manager.get_order(101))



