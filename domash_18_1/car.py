
"""Завдання 4
Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
Реалізуйте методи класу для введення-виведення даних та інших операцій."""


class Car:

    def __init__(self,model="",color="",year=0,engin=0.0,price=0.0,facture=""):
        self.model = model
        self.color = color
        self.year = year
        self.engin = engin
        self.price = price
        self.facture = facture     #    виробник

    def input_data(self):
        self.model = input("Введіть назву моделі :")
        self.color = input("Введіть колір авто :")
        self.year = input("Якого року авто :")
        self.engin = float(input("Який об'єм двигуна :"))
        self.price = float(input("Вкажіть ціну авто :"))
        self.facture = input("Хто виробник авто :")

    def print_data(self):
        print('--------Інформація про авто----------')
        print(f"Модель      : {self.model}")
        print(f"Колір       : {self.color}")
        print(f"Рік випуску : {self.year} ")
        print(f"Об'єм двигуна : {self.engin} ")
        print(f"Ціна        : {self.price}")
        print(f"Виробник    : {self.facture}")

    def change_color(self, new_color):
        self.color = new_color          #     міняємо колір

    def apply_discount(self,procent):
        if procent < 0 or procent > 100:
            print("Неправельний процент :")
            return
        discount = self.price * (procent / 100)
        self.price -= discount

    def is_older_that(self,year):
        return self.year < year


car = Car()
car.input_data()
car.print_data()

car.change_color("синій")
car.apply_discount(12)
print("\nПісля зміни кольору і знижки :")
car.print_data()


car = Car()      #     тут падало на іфі бо небачило бо тут не існувало Car()
if car.is_older_that(2015):
    print("Цец авто старше за 2015 рік :")
else:
    print("Це авто не старіше за 2015 рік .")

