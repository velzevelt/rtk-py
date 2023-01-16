from triangle_exceptions import *
from enum import Enum
import warnings


class TriangleTypes(Enum):
    ISOSCELES = "Равнобедренный"
    EQUILATERAL = "Равносторонний"
    VERSATILE = "Разносторонний"


def get_triangle_type(a: int, b: int, c: int) -> str:
    result = 'Неизвестный треугольник'

    if a <= 0 or b <= 0 or c <= 0:
        raise NonExistingTriangleError(
            "Треугольника с отрицательными или нулевыми сторонами не существует")

    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            result = TriangleTypes.EQUILATERAL.value
        elif a == b or a == c or b == c: #* 3 сторона не может быть равной из-за предыдущего условия
            result = TriangleTypes.ISOSCELES.value
        else:
            result = TriangleTypes.VERSATILE.value
    else:
        raise NonExistingTriangleError

    return result


def main():
    sides = input("Введите стороны треугольника: ")
    sides = str.split(sides, sep=" ")

    for number in sides:
        if number.isnumeric():
            sides[number] = int(number)
        else:
            sides.remove(number)
            warnings.warn("Неверный тип стороны")

    print(sides)

    #print(get_triangle_type(4, 4, 4))


if __name__ == "__main__":
    main()
