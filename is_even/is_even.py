def my_sum(n: int) -> int:
    n = abs(n)

    if n == 0:
        return n
    else:
        return n + my_sum(n - 1)


def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def main():
    try:
        x = int(input("Введите число "))
        sum = my_sum(x)
        if is_even(sum):
            print(f'{x}, {sum}, "Четно"')
        else:
            print(f'{x}, {sum}, "Нечетно"')
    except ValueError:
        print("Число не распознано")
        main()



if __name__ == "__main__":
    main()