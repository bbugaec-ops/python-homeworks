#
# """ ПОЛІМОРФІЗМ Polymorphism): Можливість об'єктів різних класів реагувати на один і той самий
#                                        виклик методу по-різному, надаючи гнучкість."""
#
# """  Абстракція (Abstraction): Приховування складних деталей реалізації
#                    та відображення лише необхідних функцій користувачеві.  """
# # num1 = 1
# # num2 = 2
# # print(num1 + num2)
# #
# # str1 = '1'
# # str2 = '2'
# # print(str1 + str2)
# #
# # print(len('python'))
# # print(len([1,2,3]))
#
# class Film:
#     def __init__(self,title,director):
#         self.title = title
#         self.director = director
#
#     def showInfo(self):
#         print(f"Film title: {self.title}")
#         print(f"Film director: {self.director}")
#
#
# class Book:
#     def __new__(cls, *args, **kwargs):
#         print("I am __new__ magic method !")
#         return super(Book,cls).__new__(cls)
#
#
#     def __init__(self, title, autor,pages):
#         print("I am __init__ method  !")
#         self.title = title
#         self.autor = autor
#         self.pages = pages
#
#     def showInfo(self):
#         print(f"Book title: {self.title}")
#         print(f"Book autor: {self.autor}")
#
#     def __str__(self):
#         return f"Книга: {self.title}, autor: {self.autor}"
#
#
#     def __eq__(self, otherObj):
#         return self.autor == otherObj.autor and self.title == otherObj.title
#
#     def __gt__(self, other):
#         if isinstance(other,Book):
#             return self.pages > other.pages
#
#     def __lt__(self, other):
#         if isinstance(other,Book):
#             return self.pages < other.pages
#
#     def __le__(self, other):
#         if isinstance(other,Book):
#             return self.pages <= other.pages
#
#     def __ge__(self, other):
#         if isinstance(other.Book):
#             return self.pages >= other.pages
#
#     def __ne__(self, other):
#         if isinstance(other.Book):
#             return self.pages != other.pages
#
#
#
# # film1 = Film('Avatar','Cameron')
# # book1 = Book('Python','Gvido')
# book2 = Book('Harry Poter','Rouling',300)
# book3 = Book('Harry Poter','Rouling',300)
# #
# # for item in (film1,book1):
# #     item.showInfo()
#
# # print(book1 + book2)
#
# book1 = Book("Python",'Gvido',300)
# print(book1)
#
# print(book3 == book2)
from гра.dict_dict import value


class Point:
    __slots__ = ('x','y','z')
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}:{self.y}"

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        return self

    def __float__(self):
        return (self.x**2 + self.y**2) ** 0.5


print(Point(2, 2) * 2.3)
print(Point(2, 2) * Point(3, 3))

p1 = Point(1, 1)
p1 += 2
print(p1)

print(float(p1))

p1.z = 1
print(p1.__slots__)


class Point3D(Point):
    __slots__ = ('z',)
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

    def __str__(self):
        return super().__str__() + f" : {self.z}"

p3 = Point3D(1,1,1)
print(p3)
print(p3.__slots__)

print('===========================')

class Circle:
    def __init__(self,r):
        self.r = r

    def __eq__(self, other):
        return self.r == other.r

    def __gt__(self, other):
        return self.r > other.r

    def __lt__(self, other):
        return self.r < other.r

    def __iadd__(self, valume):
        self.r += valume
        return self
    def __isub__(self, other):
        self.r -= value
        return self

c1 = Circle(5)
c2 = Circle(5)
c3 = Circle(3)

print(c1 == c2)
print(c1 > c3)
print(c1 < c3)