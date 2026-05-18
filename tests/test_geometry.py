"""Тесты для геометрических функций."""

import pytest

from src.geometry import (
    calculate_area,
    find_catheter_by_hypotenuse_and_angle,
    find_hypotenuse_by_legs,
    find_leg_by_hypotenuse_and_other_leg,
)


# Тесты для find_catheter_by_hypotenuse_and_angle
def test_find_catheter():
    """Тест нахождения катета через гипотенузу и угол."""
    result = find_catheter_by_hypotenuse_and_angle(10, 30)
    assert round(result, 10) == 5  # Округлить до 10 знаков
    assert round(find_catheter_by_hypotenuse_and_angle(5, 90), 10) == 5
    assert round(find_catheter_by_hypotenuse_and_angle(100, 0), 10) == 0


def test_find_catheter_invalid_hypotenuse():
    """Тест с неверным значением гипотенузы."""
    with pytest.raises(ValueError, match="Гипотенуза должна быть положительным числом"):
        find_catheter_by_hypotenuse_and_angle(-5, 30)
    with pytest.raises(ValueError):
        find_catheter_by_hypotenuse_and_angle(0, 30)


# Тесты для find_hypotenuse_by_legs
def test_find_hypotenuse():
    """Тест нахождения гипотенузы по катетам (теорема Пифагора)."""
    assert find_hypotenuse_by_legs(3, 4) == 5
    assert find_hypotenuse_by_legs(5, 12) == 13
    assert find_hypotenuse_by_legs(6, 8) == 10


def test_find_hypotenuse_invalid_legs():
    """Тест с неверными значениями катетов."""
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        find_hypotenuse_by_legs(-3, 4)
    with pytest.raises(ValueError):
        find_hypotenuse_by_legs(0, 5)


# Тесты для find_leg_by_hypotenuse_and_other_leg
def test_find_leg():
    """Тест нахождения катета по гипотенузе и другому катету."""
    assert find_leg_by_hypotenuse_and_other_leg(5, 3) == 4
    assert find_leg_by_hypotenuse_and_other_leg(13, 5) == 12
    assert find_leg_by_hypotenuse_and_other_leg(10, 6) == 8


def test_find_leg_invalid_values():
    """Тест с некорректными входными данными."""
    with pytest.raises(
        ValueError, match="Гипотенуза и катет должны быть положительными числами"
    ):
        find_leg_by_hypotenuse_and_other_leg(-5, 3)
    with pytest.raises(
        ValueError, match="Катет не может быть больше или равен гипотенузе"
    ):
        find_leg_by_hypotenuse_and_other_leg(5, 5)
    with pytest.raises(ValueError):
        find_leg_by_hypotenuse_and_other_leg(5, 6)


# Тесты для calculate_area
def test_calculate_area():
    """Тест вычисления площади."""
    assert calculate_area(3, 4) == 6
    assert calculate_area(5, 6) == 15
    assert calculate_area(2.5, 4) == 5.0


def test_calculate_area_invalid():
    """Тест с неверными значениями."""
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        calculate_area(-3, 4)
