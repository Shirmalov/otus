
from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    'side_a, side_b, side_c, area',
    [
        (4, 6, 8, 11.61895003862225),
        (7.4, 4.7, 6.9, 15.778973350633429)
    ],
    ids=['integer', 'float']
)
def test_triangle_area_positive(side_a, side_b, side_c, area, create_api):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.get_area() == area, f'Area should be {area}'


@pytest.mark.parametrize(
    'side_a, side_b, side_c, perimeter',
    [
        (3, 5, 7, 15),
        (7.4, 4.7, 6.9, 19.0)
    ],
    ids=['integer', 'float']
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter, create_api):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.get_perimeter() == perimeter, f'Perimeter should be {perimeter}'
