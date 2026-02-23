"""Завдання 2
Створіть клас Device, який містить інформацію про пристрій.

За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину),
клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).

Кожен із класів має містити необхідні для роботи методи.
"""

class Device:
    def __init__(self,brand="",model="",watts=0):
        self.brand = brand
        self.model = model
        self.watts = watts
        self.plugget = True

    def plug_in(self):
        self.plugget = True
        print(f" {self.brand} {self.model} включили")

    def unpug(self):
        self.plugget = False
        print(f" {self.brand} {self.model} виключили")

    def info(self):
        print(f"Пристрій : {self.brand} {self.model}, {self.watts} W")

    def info(self):
        print(f"--------Пристрій : {self.brand} -- модель - {self.model}, потужність - {self.watts} - W,---------")

class CoffeMashin(Device):
    def __init__(self,brand="",model="",watts="",water_ml=0):
        super().__init__(brand,model,watts)
        self.water_ml = water_ml

    def make_coffe(self):
        print("-------Кофемашина варить кофе----- ")

class Blender(Device):
    def __init__(self,brand="",model="",watts=0):
        super().__init__(brand,model,watts)

    def blend(self):
        if not self.plugget:
            print("Блендер не включений")
            return
        print("Блендер включений")
        print("-------Блендер робить------")



class Vidik(Device):
    def __init__(self,brand="",model="",watts=0,film=""):
        super().__init__(brand,model,watts)
        self.film = film

    def movie(self):
       if not self.plugget:
           print("Відік не включений :")
           return
       print("------Відік працює-------")
       print(f"Іде фільм: {self.film}")


cm = CoffeMashin(brand="Zelmer",model="CM=100", watts=1200,water_ml=500)
cm.info()
cm.make_coffe()

print('-----------')

bd = Blender(brand="Sony",model="hi-fi",watts=800)
bd.info()
bd.blend()

print('-----------')

vd = Vidik(brand="LG",model="пишущий",watts=125)
vd.info()
vd.movie()
