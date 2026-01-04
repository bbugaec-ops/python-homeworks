"""  Завдання 1
Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалі­зуйте:

перевірку на рівність типів літаків (операція = =);
збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=). """
from ast import iter_fields


class Airplane:
    def __init__(self,plane_type, max_passengers, current_passengers=0):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    #  провірка на рівність типів літаків
    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.plane_type == other.plane_type

    #  додавання віднімання пасажирів
    def __add__(self, other):
        if isinstance(other, int):
            new_count = self.current_passengers + other

            new_count = min(new_count, self.max_passengers)

            new_count = max(0, new_count)

            new_plane = Airplane(self.plane_type, self.max_passengers, new_count)
            return new_plane
        return self


    def __sub__(self, other):
        if isinstance(other, int):
            new_count = self.current_passengers - other
            new_count = max(0, new_count)

            new_plane = Airplane(self.plane_type, self.max_passengers, new_count)
            return new_plane
        return self

    def __iadd__(self, other):
        if isinstance(other,int):
            self.current_passengers += other
            self.current_passengers = min(self.current_passengers, self.max_passengers)
            self.current_passengers = max(0, self.current_passengers)
        return self

    def __isub__(self, other):
        if isinstance(other,int):
            self.current_passengers -= other
            self.current_passengers = max(0, self.current_passengers)
        return self

    def __gt__(self, other):
        if isinstance(other,Airplane):
            return self.max_passengers > other.max_passengers
        return False

    def __lt__(self, other):
        if isinstance(other,Airplane):
            return self.max_passengers < other.max_passengers
        return False

    def __ge__(self, other):
        if isinstance(other,Airplane):
            return self.max_passengers >= other.max_passengers
        return False

    def __le__(self, other):
        if isinstance(other,Airplane):
            return self.max_passengers <= other.max_passengers
        return False

    def __str__(self):
        return f"Літак {self.plane_type}: {self.current_passengers}/{self.max_passengers}"

    def __repr__(self):
        return f"Airplane('{self.plane_type}', {self.max_passengers},{self.current_passengers}"


print("="*50)
print("Завдання 1: Class Airplane з перевантаженням операторів")
print("="*50)

plane1 = Airplane("Boeing 735",150,100)
plane2 = Airplane("Airobus an- 24",180,120)
plane3 = Airplane("Mria 450",850,450)

print("\n1. Літаки:")
print(f" {plane1}")
print(f"  {plane2}")
print(f" {plane3}")

#  чи рівні
print("\n2. Перевірка на рівність типів (==):")
print(f" plane1 == plane2: {plane1 == plane2}")
print(f" plane1 == plane3: {plane1 == plane3}")

print("\n3. Збільшеня і зменьшеня пасажирів(+, -):")
plane4 = plane1 + 20
print(f" plane1 + 20 = {plane4}")

plane5 = plane2 - 35
print(f"plane3 - 35 = {plane5}")

print()
print("\n4. Збільшеня зменьшеня з присвоюваням:")
plane1 += 25
print(f"  plane1 += 25: {plane1}")

plane3 -= 15
print(f" plane3 -= 15: {plane3}")

plane3 += 200
print(f" plane3 += 350 (обмежено максимум): {plane3}")


print("\n5. Порівняти за максимальною кількістю :")
print(f"  plane1 > plane2: {plane1 > plane2}")
print(f"  plane1 < plane2: {plane1 < plane2}")
print(f"  plane1 >= plaane2: {plane1 >= plane2}")
print(f"  plane1 <= plane2: {plane1 <= plane2}")





