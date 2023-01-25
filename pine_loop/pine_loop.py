def draw_pine(char: str, height: int):
    for i in range(0, height):
        space = " " * (height - i)
        pine = char * i
        print(space + pine + pine)


def main():
    try:
        draw_char = str(input("Введите символ елки: "))
        height = int(input("Введите высоту елки: "))
        draw_pine(draw_char, height)
    except ValueError:
        main()


if __name__ == "__main__":
    main()
