


class Animal:
    def __init__(self,name,age,color,eat):
        self.name = name
        self.age = age
        self.color = color
        self.eat = eat


    def move(self):
        print("Move")

    def vois(self):
        print("Vois")

    def get_info(self):
        print(f" Name - {self.name}, Age - {self.age}, Color - {self.color}, Eat - {self.eat}")


class Dog(Animal):
    def move(self):
        print("Dog runs")

    def vois(self):
        print("Dog woof")

    def несе_палку(self):
        print("Собака несе палицю")

class Cat(Animal):
    def move(self):
        print("Cat runs")

    def vois(self):
        print("Cat mauu")

    def царапає(self):
        print("Кіт царапається")

class Bird(Animal):
    def move(self):
        print("Птах летить")

    def vois(self):
        print("Птах цвірінькає")

    def flay(self):
        print("Птах літає")


dog1 = Dog("Бім",4,"рижий","м'ясо")
cat1 = Cat("Пусік",7,"трохмастний","торти(любіме)")
bird1 = Bird("Кеша",5,"жовтий","зерно")

for x in (dog1,cat1,bird1):
    x.get_info()
    x.move()
    x.vois()




