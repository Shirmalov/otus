
from src.circle import Circle
import pytest


# Позитивные тесты
@pytest.mark.parametrize(
    'radius, area',
    [
        (8, 201.06),
        (3.7, 43.01)
    ],
    ids=['integer', 'float']
)
def test_circle_area_positive(radius, area, create_api):
    circle = Circle(radius)
    assert round(circle.get_area(), 2) == area, f'Area should be {area}'


@pytest.mark.parametrize(
    'radius, perimeter',
    [
        (5, 31.42),
        (6.5, 40.84)
    ],
    ids=['integer', 'float']
)
def test_circle_perimeter_positive(radius, perimeter, create_api):
    circle = Circle(radius)
    assert round(circle.get_perimeter(), 2) == perimeter, f'Perimeter should be {perimeter}'


# Негативные тесты
@pytest.mark.parametrize(
    'radius',
    [
        -5,
        0,
        "string",
        None,
        [],
        {}
    ],
    ids=['negative', 'zero', 'string', 'none', 'list', 'dict']
)
def test_circle_negative_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)
