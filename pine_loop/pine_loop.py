def draw_pine(char: str, height: int, outline_only: bool = False) -> str:
    if not (isinstance(char, str) or isinstance(height, int)):
        from warnings import warn
        warn("Некорректный тип входных данных")
        return False

    res = ''
    for i in range(1, height + 1):
        space = " " * (height - i)
        pine_len = i - 1

        if outline_only:
            if pine_len + 1 == height:
                res += space + char * i + char * (i - 1)
            elif pine_len != 0:
                res += space + char + (" " * pine_len) + (" " * (pine_len - 1) ) + char
            else:
                res += space + char + (" " * pine_len)
        else:
            if pine_len != 0:
                res += space + char * i + char * (i - 1)
            else:
                res += space + char * i

        res += "\n"

    return res


def main():
    try:
        # draw_char = str(input("Введите символ елки: "))
        # height = int(input("Введите высоту елки: "))
        # print(draw_pine("8", 16, outline_only=False))
        print(draw_pine("8", 16, outline_only=True))

    except ValueError:
        main()
    except NameError:
        main()



if __name__ == "__main__":
    main()
