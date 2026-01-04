""" Завдання 2
Створіть клас Flat (Квартира). Реалізуйте перевантажені оператори:

перевірку на рівність площ квартир (операція ==);
перевірку на нерівність площ квартир (операція !=);
порівняння двох квартир за ціною (операції >, <, <=, >=). """

class Flat:

    def __init__(self, area: float, price: float):
        self.area = float(area)
        self.price = float(price)

    # ==  (рівність за площею)
    def __eq__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.area == other.area

    # !=  (нерівність за площею)
    def __ne__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.area != other.area

    # Порівняння за ціною
    def __lt__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price >= other.price

    def __repr__(self):
        return f"Flat(area={self.area}, price={self.price})"

    # Приклад використання
flat1 = Flat(56.5, 78000)
flat2 = Flat(52.5, 62000)
flat3 = Flat(60, 77000)

print(flat1 == flat2)
print(flat1 != flat3)

print(flat1 < flat2)
print(flat1 >= flat3)
