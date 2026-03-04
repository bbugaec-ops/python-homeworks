# shapes_txt.py

class Shape:
    def Show(self):
        print("Shape")

    def SaveLine(self):
        return "Shape"

    @staticmethod
    def LoadLine(line: str):
        parts = line.strip().split()
        if not parts:
            return None

        t = parts[0]

        if t == "Square":
            # Square x y side
            return Square(float(parts[1]), float(parts[2]), float(parts[3]))

        if t == "Rectangle":
            # Rectangle x y w h
            return Rectangle(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]))

        if t == "Circle":
            # Circle cx cy r
            return Circle(float(parts[1]), float(parts[2]), float(parts[3]))

        if t == "Ellipse":
            # Ellipse x y w h
            return Ellipse(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]))

        raise ValueError("Unknown shape type: " + t)


class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def Show(self):
        print(f"Square: top-left=({self.x},{self.y}), side={self.side}")

    def SaveLine(self):
        return f"Square {self.x} {self.y} {self.side}"


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def Show(self):
        print(f"Rectangle: top-left=({self.x},{self.y}), w={self.w}, h={self.h}")

    def SaveLine(self):
        return f"Rectangle {self.x} {self.y} {self.w} {self.h}"


class Circle(Shape):
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r

    def Show(self):
        print(f"Circle: center=({self.cx},{self.cy}), r={self.r}")

    def SaveLine(self):
        return f"Circle {self.cx} {self.cy} {self.r}"


class Ellipse(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def Show(self):
        print(f"Ellipse: bounding top-left=({self.x},{self.y}), w={self.w}, h={self.h}")

    def SaveLine(self):
        return f"Ellipse {self.x} {self.y} {self.w} {self.h}"


def save_shapes(shapes, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for s in shapes:
            f.write(s.SaveLine() + "\n")   # важливо: \n


def load_shapes(filename):
    shapes = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            obj = Shape.LoadLine(line)
            if obj is not None:
                shapes.append(obj)
    return shapes


if __name__ == "__main__":
    shapes1 = [
        Square(10, 20, 5),
        Rectangle(0, 0, 12, 6),
        Circle(5, 5, 3),
        Ellipse(2, 2, 10, 4),
    ]

    file_name = "shapes.txt"

    save_shapes(shapes1, file_name)
    shapes2 = load_shapes(file_name)

    print("Loaded shapes:")
    for s in shapes2:
        s.Show()
