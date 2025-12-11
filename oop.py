import random


class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    #age = 20
    #name = "Nick"

    def show_info(self):
        return f"name: {self.name},age: {self.age}"


    def showMsg(self,text):
        return f"Student {self.name} says {text}"


st1 = Student('nick',55)
print(st1.show_info())

st2 = Student('bob',33)
st2.name = "Bob"
print(st2.show_info())

print(st1.showMsg("- hello !"))



print("----------------------")

class Car:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

        self.__color="red"

    def get_color(self):
        return self.color

    def show_infor(self):
        return f"name: {self.name} , age - {self.age} , color {self.color}"




car1 = Car('toyota',2015,'red -')
#car1.color = "blask"

car2 = Car("bmw",2020,'black -')

print(car1.get_color())
print(car1.show_infor())
print(car2.show_infor())

print('-----------------------------------')
import random

class Person:
    def __init__(self,name,age,salary):
        self.__name = name
        self.age = age
        self.salary = salary
        # private
        self.__personID = random.randint(1,100)

    def __getId(self):
        return f"{self.__personID}"


    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self,value):
        self.__name = value


    @property
    def personID(self):
        return self.__personID

    @personID.setter
    def personID(self):
        return self.__personID

    @personID.setter
    def personID(self,value):
        if value > 0:
            self.__personID = value



    def getInfo(self):
        return f"Name: {self.name}, age: {self.age}, salary: {self.salary}, id: {self.__getId()}"




person1 = Person('Kris',30,1000)
print(person1.name)

#print(person1.__personID)
print(person1.personID)
person1.personID = 10

person1.name = 'qwerty'
print(person1.getInfo())

print('-------------------------')

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

city = City()           # ← створення об’єкта
city.input_data()       # ← виклик методу введення даних
city.output_data()      # ← виклик методу виведення

print(city.is_megapolis())