from enum import Enum
from warnings import warn


class TriangleTypes(Enum):
    ISOSCELES = "Равнобедренный"
    EQUILATERAL = "Равносторонний"
    VERSATILE = "Разносторонний"


def get_triangle_type(a: int = None, b: int = None, c: int = None):
    result = 'Треугольник не существует'

    if a is None or b is None or c is None:
        warn("Недостаточно сторон")
        return result

    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        warn("Некорректные входные данные")
        return result

    if a <= 0 or b <= 0 or c <= 0:
        warn("Треугольник с отрицательными или нулевыми сторонами не существует")
        return result

    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            result = TriangleTypes.EQUILATERAL.value
        elif a == b or a == c or b == c:  # * 3 сторона не может быть равной из-за предыдущего условия
            result = TriangleTypes.ISOSCELES.value
        else:
            result = TriangleTypes.VERSATILE.value
    else:
        warn("Треугольник с такими сторонами не существует")

    return result


def main():
    line = input("Введите стороны треугольника: ")
    line = str.split(line, sep=" ")

    if len(line) < 3:
        print("Недостаточно сторон")
        main()
    else:
        print(get_triangle_type(line[0], line[1], line[2]))


if __name__ == "__main__":
    main()
