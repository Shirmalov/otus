
from src.rectangle import Rectangle
import pytest


# Позитивные тесты
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
    assert round(rectangle.get_area(), 2) == area, f'Area should be {area}'


@pytest.mark.parametrize(
    'width, height, perimeter',
    [
        (3, 5, 16),
        (7.4, 4.7, 24.20)
    ],
    ids=['integer', 'float']
)
def test_rectangle_perimeter_positive(width, height, perimeter, create_api):
    rectangle = Rectangle(width, height)
    assert round(rectangle.get_perimeter(), 2) == perimeter, f'Perimeter should be {perimeter}'


# Негативные тесты
@pytest.mark.parametrize(
    'width, height',
    [
        (0, 5),      # Ширина равна нулю
        (3, 0),      # Высота равна нулю
        (-1, 5),     # Отрицательная ширина
        (3, -2),     # Отрицательная высота
        (-3, -4),    # Обе стороны отрицательные
        ("abc", 5),  # Неправильный тип данных для ширины
        (3, "xyz"),  # Неправильный тип данных для высоты
        (None, 5),   # Неправильный тип данных для ширины
        (3, None)    # Неправильный тип данных для высоты
    ],
    ids=['zero_width', 'zero_height', 'negative_width', 'negative_height',
         'both_negative', 'string_width', 'string_height', 'none_width', 'none_height']
)
def test_rectangle_negative_cases(width, height):
    with pytest.raises(ValueError):
        Rectangle(width, height)
