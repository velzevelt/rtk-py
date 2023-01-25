from math import cos
from math import sin


def y(x):
    return cos(x**2) + sin(x**2)


try:
    h = int(input("Шаг функции: "))
    steps = int(input("Число шагов: "))
    steps = abs(steps)
    h = abs(h)
except ValueError:
    h = 1


for x in range(0, steps, h):
    print(f'[{x}, {y(x)}]')
