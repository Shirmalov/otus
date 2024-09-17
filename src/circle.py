
import math
from figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус круга должен быть положительным числом.")
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius

# circle = Circle(4)
# print("Площадь круга:", circle.get_area())
# print("Периметр круга:", circle.get_perimeter())
