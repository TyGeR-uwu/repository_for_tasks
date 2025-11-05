import math

class Figure:
    def area(self):
        raise NotImplementedError("Метод area() не определён в подклассе")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() не определён в подклассе")

    def compare_area(self, other):
        if self.area() > other.area():
            return "Больше"
        elif self.area() < other.area():
            return "Меньше"
        else:
            return "Равно"

    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return "Больше"
        elif self.perimeter() < other.perimeter():
            return "Меньше"
        else:
            return "Равно"


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Стороны не образуют треугольник")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


#test part
s = Square(100)
r = Rectangle(100, 20)
print(s.compare_area(r))