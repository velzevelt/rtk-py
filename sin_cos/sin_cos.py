from math import cos
from math import sin


def y(x):
    return cos(x**2) + sin(x**2)


h = int(input("Шаг функции: "))
h = abs(h)

for x in range(0, 5, h):
    print(f'[{x}, {y(x)}]')
