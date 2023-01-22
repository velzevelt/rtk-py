from math import sqrt
from warnings import warn


def solve_equation(a: int = 1, b: int = 1, c: int = 1):
    d = b ** 2 - 4 * a * c

    if any(i == 0 for i in (a, b, c)):
        warn(f"Incorrect input: {a, b, c} Zero forbidden")
        return False

    if d <= 0:
        if d == 0:
            return -b / 2 * a
        else:
            return False
    else:
        d_root = sqrt(d)
        double_a = 2 * a
        return [
            (-b + d_root) / double_a,
            (-b - d_root) / double_a
        ]


print(solve_equation(10, 5, -26))
