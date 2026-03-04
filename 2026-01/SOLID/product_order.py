"""   завдання:
      Вам потрібно розробити програму для управління замовленнями в онлайн-магазині.
  У програмі повинна бути можливість:

      Створювати замовлення.
  Розраховувати загальну вартість замовлення з урахуванням знижок.
  Генерувати рахунок-фактуру для замовлення.
  Зберігати інформацію про замовлення.
  Ваша задача — реалізувати цю програму, використовуючи принципи SOLID,
  щоб забезпечити гнучкість, розширюваність і підтримуваність коду."""

from abc import ABC, abstractmethod


# товар
class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty              #   кількість

    def total(self):
        return self.price * self.qty


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def subtotal(self):
        s = 0
        for it in self.items:        #     сума товару без знижок
            s += it.total()
        return s


# абстрактна знижка
class Discount(ABC):
    @abstractmethod
    def amount(self, order):
        pass


class NoDiscount(Discount):
    def amount(self, order):
        return 0

#   знижка
class PercentDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def amount(self, order):
        return order.subtotal() * self.percent / 100



class Pricing:
    def __init__(self, discount):
        self.discount = discount

    def total(self, order):
        total = order.subtotal() - self.discount.amount(order)
        if total < 0:
            total = 0
        return total             #  шоб небула від'ємна ціна


# формуємо текст
class Invoice:
    def generate(self, order, pricing):
        text = f"INVOICE #{order.order_id}\n"
        text += "-" * 25 + "\n"
        for it in order.items:
            text += f"{it.name}: {it.qty} x {it.price} = {it.total()}\n"
        text += "-" * 25 + "\n"
        text += f"TOTAL: {pricing.total(order)}\n"
        return text


#
class OrderRepo:
    def __init__(self):
        self.db = {}

    def save(self, order):
        self.db[order.order_id] = order

    def get(self, order_id):
        return self.db.get(order_id)


# точка входу маін - головний
if __name__ == "__main__":
    repo = OrderRepo()

    order = Order("A-001")
    order.add_item(Item("Keyboard", 500, 1))
    order.add_item(Item("Mouse", 300, 2))

    repo.save(order)

    discount = PercentDiscount(10)  # 10% знижка
    pricing = Pricing(discount)
    invoice = Invoice()

    saved = repo.get("A-001")
    print(invoice.generate(saved, pricing))
