"""

Задачка: есть массив чисел, пользователь вводит число, нужно вывести первое подмножество чисел подряд, которое в сумме дает число пользователя

"""


def main():
    ar = [i for i in range(100) if i % 2 != 0]
    print(ar)

    num = 48
    # while True:
    #     try:
    #         num = int(input("Введите желаемое число "))
    #         break
    #     except ValueError:
    #         pass
    #     except KeyboardInterrupt:
    #         return

    # counter = 0
    # for key, val in enumerate(ar):
    #     counter += val
    #     print(key, val, counter)
    #     if counter == num:
    #         print(key)
    #         break
    #     elif counter > num:
    #         counter = val
    #     elif val > num:
    #         print("Пара не найдена")
    #         break
    # else:
    #     print("Пара не найдена")


if __name__ == '__main__':
    main()
