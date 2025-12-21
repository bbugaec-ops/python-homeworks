"""     Методи класу """

import random
from datetime import date


class Person:
    hobby = 'cooking'

    def __init__(self,name,age):
        self.name = name
        self._age = age
        self.__personId = random.randint(1,1000)


    def __showID(self):
        return self.__personId

    def get_info(self):
        return f"Person name: {self.name}, age : {self._age}, id: {self.__showID()}"

    @classmethod
    def setDefaultHobby(cls,newhobby):
        cls.hobby = newhobby

    @classmethod
    def basedOnBYear(cls,name,byear):
        personAge = date.today().year - byear
        return cls(name,personAge)

    @classmethod
    def basedOnStr(cls,strInt):
        name,age = strInt.split(" ")
        return cls(name,age)


pr1 = Person("Bob",30)
print(pr1.get_info())
print(pr1.hobby)

Person.setDefaultHobby('driver')

pr2 = Person("Djon",22)
print(pr2.get_info())
print(pr2.hobby)

print(pr1.hobby)

pr3 = Person.basedOnBYear("Lola",2000)
print(pr3.get_info())

pr4 = Person.basedOnBYear("Max",45)
print(pr4.get_info())


class Developer(Person):
    def __init__(self,name,age,jobTitle):
        super().__init__(name, age)
        self.jobTitle = jobTitle
        self.__salary = 0


    def setBasicSalary(self):
        if self.__rung == 'junior':
            self.__salary = 1000
        elif self.__rung == 'middle':
            self.__salary = 2000
        elif self.__rung == 'senior':
            self.__salary = 5000

    @classmethod
    def setRung(cls,rung):
        cls.__rung = rung

    def getInfo(self):
        return super().get_info() + f"\njob title: {self.jobTitle},\nrung: {self.__rung}, \nsalary: {self.__salary} "

    def calcSalary(self,perc):
        return self.__salary + self.__salary * perc


jun1 = Developer("Bill",23,"frontemd")
Developer.setRung("middle")
#jun1.setBasicSalary()

jun2 = Developer("Joe",33,"backend")

#print(jun1.__dict__)

for jun in zip((jun1,jun2),(0.1,0.3)):

    jun[0].setBasicSalary()
    print(jun[0].getInfo())
    print(f"Expected salary : {jun[0].calcSalary(jun[1])}")

print('--------------------------------------------------')
""" Множинне успадкування """
class Book:
    def __init__(self,title,autor,papers):
        self.title = title
        self.autor = autor
        self.papers = papers

    def showBookInfo(self):
        print("Title: ",self.title)
        print("Autor:", self.autor)
        print("Paper:",self.papers)

class File:
    def __init__(self,fileSize,src):
        self.fileSize = fileSize
        self.src = src

    def showFileProps(self):
        print("File size:",self.fileSize)
        print("File src:",self.src)

class Ebook(Book,File):
    def __init__(self,title,autor,papers,fileSize,src):
        Book.__init__(self,title,autor,papers)
        File.__init__(self,fileSize,src)





ebook1 = Ebook("python","qvido",400,123,"C://book.txt")
ebook1.showBookInfo()
ebook1.showFileProps()
print(Ebook.mro())

print('-------------------------')

class Flyer:
    def fly(self):
        print("Вмію літати")


class Swimmer:
    def swim(self):
        print("вмію плавати ")


class Duck(Flyer,Swimmer):
    def move(self):
        self.fly()
        self.swim()


duck = Duck()
duck.move()

print()


class Engine:
    def __init__(self,power):
        self.power = power

class Battery:
    def __init__(self,capacity):
        self.capacity = capacity


class HybridCar(Ebook,Battery):
    def __init__(self,power,capacity):
        Engine.__init__(self,power)
        Battery.__init__(self,capacity)


    def specs(self):
        print(f"Engine power: {self.power} ")
        print(f"Batteery capacity: {self.capacity} ")

car = HybridCar(150,50)
car.specs()

print('------')

class BaseUser:
    def get_permissions(self):
        return ["read"]

class AdminUser(BaseUser):
    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append("admin")
        return permissions

class ModeratorUser(BaseUser):
    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append("moderate")
        return permissions

class SuperUser(AdminUser,ModeratorUser):
    def get_permissions(self):
        return super().get_permissions()



user = SuperUser()
print(user.get_permissions())





