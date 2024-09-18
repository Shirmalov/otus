
from src.triangle import Triangle
import pytest


# Позитивные тесты
@pytest.mark.parametrize(
    'side_a, side_b, side_c, area',
    [
        (4, 6, 8, 11.62),
        (7.4, 4.7, 6.9, 15.78)
    ],
    ids=['integer', 'float']
)
def test_triangle_area_positive(side_a, side_b, side_c, area, create_api):
    triangle = Triangle(side_a, side_b, side_c)
    assert round(triangle.get_area(), 2) == area, f'Area should be {area}'


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
    assert round(triangle.get_perimeter(), 2) == perimeter, f'Perimeter should be {perimeter}'


# Негативные тесты
@pytest.mark.parametrize(
    'side_a, side_b, side_c',
    [
        (1, 2, 3),  # Сумма двух сторон равна третьей
        (1, 1, 3),  # Одна сторона больше суммы двух других
        (0, 4, 5),  # Отрицательная сторона
        (-1, 2, 3)  # Отрицательная сторона
    ],
    ids=['sum_equal', 'one_greater', 'zero_side', 'negative_side']
)
def test_triangle_negative_cases(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
