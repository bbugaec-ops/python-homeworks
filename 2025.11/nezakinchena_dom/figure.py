from rectang import Rectangle, Square, Circle



rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)
print(rect1.get_area(), rect2.get_area())


sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_area(), sq2.get_area())

cirk1 = Circle(3)
cirk2 = Circle(2)
print(cirk1.get_area(), cirk2.get_area())


figures = [rect1,rect2,sq1,sq2,cirk1,cirk2]
for figure in figures:
    print(figure.get_area())