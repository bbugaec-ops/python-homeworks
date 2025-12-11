
"""Завдання 2
Створіть клас «Місто». Збережіть у класі: назву міста, назву регіону, назву країни, кількість жителів у місті, поштовий індекс міста,
телефонний код міста. Реалізуйте методи класу для введення-виведення даних та інших операцій.
Написати метод is_valid_zipcode, який повертає True якщо __zipcode містить 5 цифр."""


class City:
    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.name = input("Введіть назву міста: ")
        self.region = input("Введіть назву регіону: ")
        self.country = input("Введіть назву країни: ")
        self.population = int(input("Введіть кількість жителів: "))
        self.postal_code = input("Введіть поштовий індекс: ")
        self.phone_code = input("Введіть телефонний код: ")

    def output_data(self):
        print("\nІнформація про місто:")
        print(f"Місто: {self.name}")
        print(f"Регіон: {self.region}")
        print(f"Країна: {self.country}")
        print(f"Населення: {self.population}")
        print(f"Поштовий індекс: {self.postal_code}")
        print(f"Телефонний код: {self.phone_code}")

    def is_megapolis(self):
        return self.population > 1_000_000

    def is_valid_zipcode(self):
        return self.postal_code.isdigit() and len(self.phone_code) == 5


city = City()
city.input_data()
city.output_data()

print("\nМегаполіс :",city.is_megapolis())
print("Коректний індекс :", city.is_valid_zipcode())

