""" Завдання 5
Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки. У класі має знаходитися два статичні методи:
 для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розра­хувати кількість
підрахунків температури та повернути це значення статичним методом.
"""

class Temperatur:
    _count = 0

    @staticmethod            #   Не требує ніякого об'єкта
    def c_to_f(c):
        Temperatur._count += 1
        return c * 9 / 5 + 32



    @staticmethod
    def f_to_c(f):
        Temperatur._count += 1
        return (f - 32) * 5 / 9

    @staticmethod
    def get_count():
        return Temperatur._count

print(Temperatur.c_to_f(0))
print(Temperatur.f_to_c(212))
print("Кількість розрахунків :", Temperatur.get_count())



# celsius = float(input("Введіть температуру в градусах :"))
# fahrenheit = (celsius * 9 / 5) + 32
# print(f"Температура {celsius} C дорівнює {fahrenheit:.1f} F")

