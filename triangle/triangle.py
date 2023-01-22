from enum import Enum
from warnings import warn


class TriangleType(Enum):
    ISOSCELES = "Равнобедренный"
    EQUILATERAL = "Равносторонний"
    VERSATILE = "Разносторонний"


def get_triangle_type(a: int = None, b: int = None, c: int = None):
    '''
    Определяет тип треугольника по трем сторонам. 
    Возвращает False, если не удается определить тип
    '''

    if a is None or b is None or c is None:
        warn("Недостаточно сторон")
        return False

    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        warn("Некорректные входные данные")
        return False

    # Треугольник с отрицательными или нулевыми сторонами не существует
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Треугольник с такими сторонами не существует
    triangle_exist = (a < b + c) and (b < a + c) and (c < a + b)
    if not triangle_exist:
        return False

    if a == b == c:
        result = TriangleType.EQUILATERAL.value
    elif a == b or a == c or b == c:
        result = TriangleType.ISOSCELES.value
    else:
        result = TriangleType.VERSATILE.value

    return result


def main():
    line = input("Введите стороны треугольника: ")
    line = str.split(line, sep=" ")

    try:
        print(get_triangle_type(line[0], line[1], line[2]))
    except IndexError:
        print("Недостаточно сторон")
        main()


if __name__ == "__main__":
    main()
