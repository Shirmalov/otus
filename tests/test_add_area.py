import pytest
import math
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


def test_add_area_circle():
    circle1 = Circle(1)
    circle2 = Circle(2)
    assert round(circle1.add_area(circle2), 5) == round(5 * math.pi, 5)


def test_add_area_rectangle():
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(5, 6)
    assert rect1.add_area(rect2) == 42


def test_add_area_square():
    square1 = Square(2)
    square2 = Square(3)
    assert square1.add_area(square2) == 13


def test_add_area_triangle():
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(5, 12, 13)
    assert triangle1.add_area(triangle2) == 36


def test_add_area_invalid_figure():
    rect = Rectangle(3, 4)
    with pytest.raises(ValueError):
        rect.add_area("not_a_figure")