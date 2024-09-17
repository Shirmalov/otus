
from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    'radius, area',
    [
        (8, 201.06192982974676),
        (3.7, 43.008403427644275)
    ],
    ids=['integer', 'float']
)
def test_circle_area_positive(radius, area, create_api):
    circle = Circle(radius)
    assert circle.get_area() == area, f'Area should be {area}'


@pytest.mark.parametrize(
    'radius, perimeter',
    [
        (5, 31.41592653589793),
        (6.5, 40.840704496667314 )
    ],
    ids=['integer', 'float']
)
def test_circle_perimeter_positive(radius, perimeter, create_api):
    circle = Circle(radius)
    assert circle.get_perimeter() == perimeter, f'Perimeter should be {perimeter}'
