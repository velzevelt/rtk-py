"""

Задачка: есть массив чисел, пользователь вводит число, нужно вывести первое подмножество чисел подряд, которое в сумме дает число пользователя

"""


def main():
    ar = [i for i in range(100) if i % 2 != 0]
    print(ar)

    # num = 8
    while True:
        try:
            num = int(input("Введите желаемое число "))
            break
        except ValueError:
            pass
        except KeyboardInterrupt:
            return

    for key, val in enumerate(ar):
        if key == 0:
            continue
        prev = ar[key - 1]
        if val + prev == num:
            print(prev, val)
            break

    else:
        print("Пара не найдена")


if __name__ == '__main__':
    main()
