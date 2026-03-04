"""
Завдання 3
Створіть клас Ship, який містить інформацію про кораблі. За допомогою механізму успадкування реалізуйте клас Frigate
(містить інформацію про фрегат), клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію про крейсер).

Кожен із класів має містити необхідні для роботи методи. """


class Ship:
    def __init__(self,name="",country="",speed=0):
        self.name = name
        self.country = country
        self.speed = speed
        self.at_sea = False

    def info(self):
        print(f" {self.name} ({self.country}), швидкість: {self.speed} вузлів")


    def sail(self):
        self.at_sea = True
        print(f"{self.name} вийшов в море")

    def stop(self):
        self.at_sea = False
        print(f"{self.name} зупинився")


class Frigat(Ship):
    def __init__(self,name="",country="",speed=0,missiles=0):
        super().__init__(name,country,speed)
        self.missiles = missiles

    def atack(self):
        if self.missiles > 0:
            self.missiles -= 1
            print(f"Фрегат {self.name} пускає ракети . Осталось {self.missiles}")
        else:
            print(f"У фрегата {self.name} нема ракет")


class Destroyer(Ship):
    def __init__(self,name="",country="",speed=0,torpeda=0):
        super().__init__(name,country,speed)
        self.torpeda = torpeda

    def atack(self):
        if self.torpeda > 0:
            self.torpeda -= 1
            print(f"Есмінець {self.name} зупинив торпеду, осталось {self.torpeda}")
        else:
            print(f"У есмінця {self.name} нема торпед")

class Cruiser(Ship):
    def __init__(self,name="",country="",speed=0,cannons=0):
        super().__init__(name,country,speed)
        self.cannons = cannons

    def atack(self):
        if self.cannons > 0:
            print(f"Крейсер {self.name} стріляє {self.cannons}")
        else:
            print(f"У крейсера {self.name} закінчились набої")



f = Frigat("------Гетьман Сагайдачний :","Ukraine",88,missiles=100)
d = Destroyer("------Storm","USA",32,torpeda=6)
c = Cruiser("-----Avrora","Rus-pigs",18,cannons=3)

f.info()
f.sail()
f.atack()

print('---------------')

d.info()
d.sail()
d.atack()

print('------------------')

c.info()
c.sail()
c.atack()


