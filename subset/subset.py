"""

Задачка: есть массив чисел, пользователь вводит число, нужно вывести первое подмножество чисел подряд, которое в сумме дает число пользователя

"""


def main():
    ar = [i for i in range(1000) if i % 2 != 0]
    print(ar)

    # num = 1996
    while True:
        try:
            num = int(input("Введите желаемое число "))
            break
        except ValueError:
            pass
        except KeyboardInterrupt:
            return

    length = len(ar)
    for key, val in enumerate(ar):
        next_key = key + 1
        if next_key > length - 1:
            continue

        tmp = val
        subset = [val]

        # Здесь length == length - 1, так как конец не включается
        for i in ar[next_key:length]:
            tmp += i
            subset.append(i)
            if tmp == num:
                print(f'{subset} => {num}')
                return
            elif tmp > num:
                break
    else:
        print("Пара не найдена")


if __name__ == '__main__':
    main()
