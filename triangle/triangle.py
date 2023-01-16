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
        elif a == b or a == c or b == c:  # * 3 сторона не может быть равной из-за предыдущего условия
            result = TriangleTypes.ISOSCELES.value
        else:
            result = TriangleTypes.VERSATILE.value
    else:
        raise NonExistingTriangleError

    return result


def main():
    line = input("Введите стороны треугольника: ")
    line = str.split(line, sep=" ")

    sides = []
    for number in line:
        try:
            sides.append(int(number))
        except ValueError:
            warnings.warn("Некоррентый тип в исходных данных")

    if len(sides) < 3:
        raise TooFewSidesError

    # print(sides)
    print(get_triangle_type(line[0], line[1], line[2]))


if __name__ == "__main__":
    # main()
    data = ( 
        
        (1, 1, 1), 
        (2, 2, 2) 
        
        )
    
    for val in data:
        triangle = val
        print(triangle)
