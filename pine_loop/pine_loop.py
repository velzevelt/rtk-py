def draw_pine(char: str, height: int) -> str:
    if not (isinstance(char, str) or isinstance(height, int)):
        from warnings import warn
        warn("Некорректный тип входных данных")
        return False

    res = ''
    for i in range(0, height):
        space = " " * (height - i)
        pine = char * i
        res += space + pine + pine + "\n"
    return res


def main():
    try:
        draw_char = str(input("Введите символ елки: "))
        height = int(input("Введите высоту елки: "))
        print(draw_pine(draw_char, height))
    except ValueError:
        main()
    except NameError:
        main()



if __name__ == "__main__":
    main()
