dictionary = {
    0: "Ноль",
    1: "Один",
    2: "Два",
    3: "Три",
    4: "Четыре",
    5: "Пять",
    6: "Шесть",
    7: "Семь",
    8: "Восемь",
    9: "Девять"
}


def main():
    try:
        x = int(input("Введите число: "))
        if x in dictionary:
            print(dictionary[x])
        else:
            print("Я не знаю это число")
    except ValueError:
        print("Число не распознано")
        main()



if __name__ == "__main__":
    main()
