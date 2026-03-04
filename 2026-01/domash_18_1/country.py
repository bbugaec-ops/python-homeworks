
"""Завдання 3
Створіть клас «Країна». Збережіть у класі: назву країни, назву континенту, кількість жителів країни, телефонний код країни, назву столиці,
назву міст країни. Реалізуйте методи класу для введення-виведення даних та інших операцій."""

class Country:
    def __init__(self,name="",continent="",population="",phone_code="",capital="",cities=None):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities if cities is not None else []

    def input_data(self):
        self.name = input("введіть країну ")
        self.continent = input("введіть континент :")

        while True:
              try:
                  self.population = int(input("ведіть кількість людей в країні "))
                  break
              except ValueError:
                  print("введіть число :")

        while True:

            self.phone_code = input("введіть телефонний код країни :")
            if self.phone_code.isdigit():
                break
            else:

                print("введіть тільки числа :")
        while True:
            self.capital = input("введіть назву столиці :")
            if self.capital.isalpha() :
                break
            else:
                print("введіть тільки букви ")


        while True:
              try:
                  city_count = int(input("Скільки міст хочете додати ? :"))
                  break
              except ValueError:
                  print("введіть число а не текст :")
        self.cities = []
        for _ in range(city_count):
            city_name = input("введіть назву міста :")
            self.cities.append(city_name)

    def output_data(self):
        print("\n--------Інформація про країну------------")
        print(f"Країна: {self.name}")
        print(f"Континент: {self.continent}")
        print(f"Населення: {self.population}")
        print(f"Телефоний код: {self.phone_code}")
        print(f"Столиця: {self.capital}")
        print("Міста країни:", ",".join(self.cities))

    def add_city(self,city_name):
        self.cities.append(city_name)


country = Country()
country.input_data()
country.output_data()