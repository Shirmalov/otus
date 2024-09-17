
from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    'width, height, area',
    [
        (3, 5, 15),
        (7.4, 4.7, 34.78)
    ],
    ids=['integer', 'float']
)
def test_rectangle_area_positive(width, height, area, create_api):
    rectangle = Rectangle(width, height)
    assert rectangle.get_area() == area, f'Area should be {area}'


@pytest.mark.parametrize(
    'width, height, perimeter',
    [
        (3, 5, 16),
        (7.4, 4.7, 24.200000000000003)
    ],
    ids=['integer', 'float']
)
def test_rectangle_perimeter_positive(width, height, perimeter, create_api):
    rectangle = Rectangle(width, height)
    assert rectangle.get_perimeter() == perimeter, f'Perimeter should be {perimeter}'
