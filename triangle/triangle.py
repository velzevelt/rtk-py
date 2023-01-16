from enum import Enum
from warnings import warn


class TriangleTypes(Enum):
    ISOSCELES = "Равнобедренный"
    EQUILATERAL = "Равносторонний"
    VERSATILE = "Разносторонний"


def get_triangle_type(a: int, b: int, c: int):
    result = 'Неизвестный треугольник'

    if any(a, b, c) is None:
        warn("Недостаточно сторон")
        return result
    elif any(a, b, c) <= 0:
        warn("Треугольника с отрицательными или нулевыми сторонами не существует")
        return result
    
    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            result = TriangleTypes.EQUILATERAL.value
        elif a == b or a == c or b == c:  # * 3 сторона не может быть равной из-за предыдущего условия
            result = TriangleTypes.ISOSCELES.value
        else:
            result = TriangleTypes.VERSATILE.value
    else:
        warn("Треугольника с такими сторонами не существует")

    return result


def main():
    line = input("Введите стороны треугольника: ")
    line = str.split(line, sep=" ")

    sides = []
    for number in line:
        try:
            sides.append(int(number))
        except ValueError:
            warn("Некоррентый тип в исходных данных")

    
    print(get_triangle_type(line[0], line[1], line[2]))


if __name__ == "__main__":
    # main()
    data = ( 
        
        (1, 1, 1),
        (1, 1), 
        (2, 2, 2),
        (0, 0, 0) 
        
        )
    
    for val in data:
        print(get_triangle_type(val[0], val[1], val[2]))        
