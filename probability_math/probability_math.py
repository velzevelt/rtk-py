from functools import lru_cache


@lru_cache(maxsize=128)
def factorial(n):
    if n < 0:
        raise ArithmeticError
    else:
        if n == 1 or n == 0:
            return 1
        else:
            return n * factorial(n - 1)


def count_permutations(n):
    return factorial(n)


def count_placements(n, k):
    return factorial(n) // factorial(n - k)


def count_combinations(n, k):
    return factorial(n) // factorial(n-k) * factorial(k)


print(count_permutations(4))
print(count_placements(4, 2))
print(count_combinations(4, 2))
