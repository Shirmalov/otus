
from src.square import Square
import pytest


@pytest.mark.parametrize(
    'side, area',
    [
        (5, 25),
        (5.9, 34.81)
    ],
    ids=['integer', 'float']
)
def test_square_area_positive(side, area, create_api):
    square = Square(side)
    assert square.get_area() == area, f'Area should be {area}'


@pytest.mark.parametrize(
    'side, perimeter',
    [
        (4, 16),
        (6.3, 25.2 )
    ],
    ids=['integer', 'float']
)
def test_square_perimeter_positive(side, perimeter, create_api):
    square = Square(side)
    assert square.get_perimeter() == perimeter, f'Perimeter should be {perimeter}'
