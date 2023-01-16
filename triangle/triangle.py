from triangle_exceptions import *
from enum import Enum

class TriangleTypes(Enum):
    ISOSCELES = "Равнобедренный"
    EQUILATERAL = "Равносторонний"
    VERSATILE = "Разносторонний"


def get_triangle_type(a: int, b: int, c: int) -> str:
    result = 'Неизвестный треугольник'

    if a <= 0 or b <= 0 or c <= 0:
        raise NonExistingTriangleError("Треугольника с отрицательными или нулевыми сторонами не существует")

    if (a < b + c) and (b < a + c) and (c < a + b):
        pass
    else:
        raise NonExistingTriangleError
            

    return result


def main():
    print(get_triangle_type(-2, 1, 1))


if __name__ == "__main__":
    main()