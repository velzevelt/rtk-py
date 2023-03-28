"""

Задачка: есть массив чисел, пользователь вводит число, нужно вывести первое подмножество чисел подряд, которое в сумме дает число пользователя

"""


def main():
    ar = [i for i in range(100) if i % 2 != 0]
    print(ar)

    num = 15
    # while True:
    #     try:
    #         num = int(input("Введите желаемое число "))
    #         break
    #     except ValueError:
    #         pass
    #     except KeyboardInterrupt:
    #         return

    closest = 0
    last = 0
    for key, val in enumerate(ar):
        if key == 0:
            continue

        prev = ar[key - 1]
        step = prev + val
        if step == num:
            print(prev, val)
            break
        elif step > num:
            break
        else:
            last = val
            closest = step
    t = num - closest
    if t in ar:
        print(t, last)
    else:
        print("Пара не найдена")


if __name__ == '__main__':
    main()
