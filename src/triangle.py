
import math
from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("С указанными сторонами треугольник создать нельзя.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


# triangle = Triangle(7, 4, 9)
# print("Площадь треугольника:", triangle.get_area())
# print("Периметр треугольника:", triangle.get_perimeter())
