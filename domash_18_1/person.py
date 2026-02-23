"""Завдання 1
Реалізуйте клас «Людина». Збережіть у класі: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
Реалізуйте методи класу для введення-виведення даних та інших операцій.
Додати метод is_major, який повертає True, якщо людина повнолітня (більше або одно 18 років) інакше False."""

from datetime import datetime

class Person:
    def __init__(self):
        print("Введіть інформацію:")
        self.input_data()


    def input_data(self):
        self.full_name = input("Введіть ПІБ :")
        self.birth_day = int(input("День народження (1-31):"))
        self.birth_month = int(input("місяць народження (1-12)"))
        self.birth_year = int(input("рік народження):"))
        self.phone = int(input("введіть номер телефону :"))
        self.city = input("введіть місто :")
        self.country = input("введіть країну :")
        self.address = input("введіть адресу :")

    def show_info(self):
        print("\n-------Інформація-------")
        print("ПІБ:, self.full_name")
        print(f"Дата народження: {self.birth_day}.{self.birth_month}.{self.birth_year}")
        print("Телефон: ,self.phone")
        print("Місто:, self.city")
        print("Країна: ,self.country")
        print("Адреса:, self.address")


    def is_major(self):
        today = datetime.today()
        age = today.year - self.birth_year

        if (today.month, today.day) < (self.birth_month, self.birth_day):
            age -= 1
        return age >= 18


p = Person()
p.show_info()
print("\nПовнолітній ?:",p.is_major())
