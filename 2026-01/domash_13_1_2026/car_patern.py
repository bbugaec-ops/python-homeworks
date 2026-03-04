"""  1. Реалізуйте клас для побудови автомобіля, де можна задати такі характеристики:

Марка автомобіля (наприклад, "Tesla", "BMW").
Тип кузова (наприклад, "седан", "позашляховик").
Колір.
Тип двигуна (наприклад, "електричний", "дизельний", "бензиновий").
Кількість дверей.
Наявність додаткових опцій (наприклад, "панорамний дах", "шкіряний салон", "автопілот").

Завдання:
Реалізуйте клас Car для представлення автомобіля.
Реалізуйте клас CarBuilder, який дозволяє поетапно будувати автомобіль.
Напишіть клас Director, який керує побудовою автомобіля.
Продемонструйте тестування створених класів, побудувавши кілька автомобілів із різними характеристиками. """


class Car:
    def __init__(self):
        self.brand = None
        self.body_type = None
        self.color = None
        self.engine_type = None
        self.doors = None
        self.options = []

    def __str__(self):
        return (
            f"Car(\n"
            f"brand = {self.brand}, \n"
            f"body_type = {self.body_type}, \n"
            f"color = {self.color}, \n"
            f"engine_type = {self.engine_type}, \n"
            f"doors = {self.doors}, \n"
            f"options = {self.options}, \n"
        )


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self,brand):
        self.car.brand = brand
        return self

    def set_body_type(self,body_type):
        self.car.body_type = body_type
        return self

    def set_color(self,color):
        self.car.color = color
        return self

    def set_engine_type(self,engine_type):
        self.car.engine_type = engine_type
        return self

    def set_doors(self,doors):
        self.car.doors = doors
        return self

    def add_options(self,options):
        self.car.options.append(options)
        return self

    def build(self):
        car = self.car
        self.car = Car()
        return car


class Director:
    def __init__(self,builder:CarBuilder):
        self.builder = builder

    def build_electric_sedan(self):
        return (
            self.builder
            .set_brand("Tesla")
            .set_body_type("sedan")
            .set_color('чорний')
            .set_engine_type("електричний")
            .set_doors(4)
            .add_options("автопілот")
            .add_options("запуск двигуна голосом зазяїна")
            .build()
        )

    def build_diesel(self):
        return (
            self.builder
            .set_brand("Merssedess")
            .set_body_type("джип")
            .set_color("blask")
            .set_engine_type("дізель")
            .set_doors(5)
            .add_options("повний привід")
            .add_options("либідка")
            .add_options("причіп з лодкою")
            .build()
        )

builder = CarBuilder()
director = Director(builder)

car1 = director.build_electric_sedan()
print(car1)

print('-------------')

car2 = (
    CarBuilder()
    .set_brand("Audi")
    .set_body_type("sedan")
    .set_color("білий")
    .set_engine_type("patrol")
    .set_doors(4)
    .add_options("круїз-контроль")
    .add_options("підігрів сидінь")
    .build()
)
print(car2)