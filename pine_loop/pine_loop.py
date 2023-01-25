# draw_char = str(input("Введите символ: "))
# height = int(input("Введите высоту елки: "))

# DEBUG ONLY
draw_char = '*'
height = 16


def draw_pine(char: str, height: int):
    for i in range(0, height):
        space = " " * (height - i)
        pine = char * i
        print(space + pine + pine)


draw_pine(draw_char, height)
