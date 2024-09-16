
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError("Метод get_area() должен быть реализован в подклассе.")

    @abstractmethod
    def get_perimeter(self):
        raise NotImplementedError("Метод get_perimeter() должен быть реализован в подклассе.")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Переданная фигура должна быть экземпляром класса Figure.")
        return self.get_area() + figure.get_area()