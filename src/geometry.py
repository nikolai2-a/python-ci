"""Модуль с геометрическими функциями для вычисления элементов прямоугольного треугольника."""

import math


def find_catheter_by_hypotenuse_and_angle(
    hypotenuse: float, angle_degrees: float
) -> float:
    """
    Вычисляет катет по гипотенузе и прилежащему углу.

    Args:
        hypotenuse: Длина гипотенузы
        angle_degrees: Величина угла в градусах (между гипотенузой и искомым катетом)

    Returns:
        Длина катета
    """
    if hypotenuse <= 0:
        raise ValueError("Гипотенуза должна быть положительным числом")
    angle_radians = math.radians(angle_degrees)
    return hypotenuse * math.sin(angle_radians)


def find_hypotenuse_by_legs(leg1: float, leg2: float) -> float:
    """
    Вычисляет гипотенузу по двум катетам (теорема Пифагора).

    Args:
        leg1: Длина первого катета
        leg2: Длина второго катета

    Returns:
        Длина гипотенузы
    """
    if leg1 <= 0 or leg2 <= 0:
        raise ValueError("Катеты должны быть положительными числами")
    return math.sqrt(leg1**2 + leg2**2)


def find_leg_by_hypotenuse_and_other_leg(hypotenuse: float, known_leg: float) -> float:
    """
    Вычисляет второй катет по гипотенузе и известному катету.

    Args:
        hypotenuse: Длина гипотенузы
        known_leg: Длина известного катета

    Returns:
        Длина второго катета
    """
    if hypotenuse <= 0 or known_leg <= 0:
        raise ValueError("Гипотенуза и катет должны быть положительными числами")
    if known_leg >= hypotenuse:
        raise ValueError("Катет не может быть больше или равен гипотенузе")
    return math.sqrt(hypotenuse**2 - known_leg**2)


def calculate_area(leg1: float, leg2: float) -> float:
    """
    Вычисляет площадь прямоугольного треугольника.

    Args:
        leg1: Первый катет
        leg2: Второй катет

    Returns:
        Площадь треугольника
    """
    if leg1 <= 0 or leg2 <= 0:
        raise ValueError("Катеты должны быть положительными числами")
    return (leg1 * leg2) / 2
