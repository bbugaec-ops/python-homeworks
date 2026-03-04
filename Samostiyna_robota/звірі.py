# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.__id = 0
#         self._protected_prop = 1
#
#     def speak(self):
#         print("some sound!")
#
#     def get_info(self):
#         return  f"Name: {self.name}"
#
#     @property
#     def protwcted_prop(self):
#         return self._protected_prop
#
#
# class Cat(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#
#
#     def speak(self):
#         print("mau mau")
#
#     def get_info(self):
#         return super().get_info() + f"\nage : {self.age}"
#
#
# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#
#     def speak(self):
#         print("gav gav")
#
#     def guard_house(self):
#         print(f'{self.name} start guard house !')
#
#
#     def get_info(self):
#         return super().get_info() + f"\nage : {self.age}"
#
#
# class Cow(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#
#
#     def speak(self):
#         print("mu mu")
#
#     def get_info(self):
#         return super().get_info() + f"\nage : {self.age}"
#
#
#
#
#
#
#
# cat1 = Cat("murzik",10)
# cat1.speak()
# print(cat1.name)
# #cat1._protected_prop = 2
# print(cat1._protected_prop)
# print(cat1.get_info())
#
# print('----------------')
#
# dag1 = Dog("sharik",5)
# dag1.speak()
# print(dag1.get_info())
#
# print('--------------------')
#
# cow1 = Cow("mashka",12)
# cow1.speak()
# print(cow1.get_info())

#
# import math
#
# class Shape:
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius * self.radius
#
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return math.pi * self.width * self.height
#
#
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#
# c = Circle(3)
# r = Rectangle(4,5)
# t = Triangle(6,2)
#
# print(c.area())
# print(r.area())
# print(t.area())
#
# #
#
# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
#
# class Admin(User):
#     def delite_user(self,user):
#         print(f"Адмін {self.username} видаляє {user.username}")
#
# class Moderator(User):
#     def __init__(self, user):
#         print(f"Модератор {self.username} банить юсера {user.username}")
#
# class RegularUser(User):
#     def __init__(self,text):
#         print(f"{self.username} коментар {text}")
#
# #
#
# admin = Admin("admin1","sjduku.com")
# mod = Moderator("mod1","yjyjrhf.com")
# user = RegularUser("alex","dhdjuk,.com")
#
#
#
#
#
#
#
#
#
# class MathTools:
#
#     @staticmethod
#     def add(a,b):
#         return a + b
#
#
# class User:
#     def __init__(self,name,age):
#         self.name = name
#         if not User.is_valid_age(age):
#             raise ValueError("Age must be positive !")
#         self.age = age
#
#     @staticmethod
#     def is_valid_age(age):
#         return age > 0
#
#
# user1 = User('Maks',23)
# print(User.is_valid_age(-10))
#
#


class Validator:
    @staticmethod
    def is_email(text):
        return "@" in text and "." in text


print(Validator.is_email("test@gmail.com"))
print(Validator.is_email("текст "))





# class Cat:
#     def __init__(self,name,age,color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,value):
#         self.__age = value
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self,value):
#         self.__color = value
#
# class Dog:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__age = value
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, value):
#         self.__color = value
#
# class Cow:
#     class Cat:
#         def __init__(self, name, age, color):
#             self.__name = name
#             self.__age = age
#             self.__color = color
#
#         @property
#         def name(self):
#             return self.__name
#
#         @name.setter
#         def name(self, value):
#             self.__name = value
#
#         @property
#         def age(self):
#             return self.__age
#
#         @age.setter
#         def age(self, value):
#             self.__age = value
#
#         @property
#         def color(self):
#             return self.__color
#
#         @color.setter
#         def color(self, value):
#             self.__color = value
#
#
#
#
#
