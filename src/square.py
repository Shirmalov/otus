
from figure import Figure


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом.")
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

# square = Square(4)
# print("Площадь квадрата:", square.get_area())
# print("Периметр квадрата:", square.get_perimeter())
