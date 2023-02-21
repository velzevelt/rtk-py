"""
Дан прямоугольник с размерами 425Х131. От него отрезают квадраты со стороной 131, пока это возможно.
Затем от оставшегося прямоугольника вновь отрезают квадраты со стороной, равной 425-131*3=32, и т.д.
На какие квадраты и в каком их количестве будет разрезан исходный прямоугольник?

1) Отрезаем 3 квадрата со стороной 131, остается прямоугольник со сторонами 131*32
2) Отрезаем 4 квадрата со стороной 32 ,(131-4*32 = 3), остается прямоугольник со сторонами 3*32
3) Отрезаем 10 квадратов со стороной 3 (32-10*3=2), остается прямоугольник со сторонами 2*3
4) Отрезаем квадрат со стороной 2 ,(3-2*1) остается прямоугольник со сторонами 1*2
5) Разрезаем на 2 квадрата со сторой 1
Итого получили: 3 квадрата 131*131; 4 квадрата - 32*32; 10 квадратов - 3*3,
1 квадрат - 2*2; 2 кадрата - 1*1


"""

init_rect = [425, 131]
big_side = max(init_rect)
small_side = min(init_rect)

result = []
while True:
    if small_side != 0:
        # Здесь может сформироваться несуществующий прямоугольник [1, 0]
        # Этот последний прямоугольник, неободим для выхода из цикла
        new_rect = [small_side, big_side % small_side]
        # print(new_rect)

        new_square = [small_side, small_side]
        result.append([big_side // small_side, new_square])

        big_side = max(new_rect)
        small_side = min(new_rect)
    else:
        break

# for square in result:
#     print(f'Количество: {square[0]}, Квадрат: {square[1]}')
