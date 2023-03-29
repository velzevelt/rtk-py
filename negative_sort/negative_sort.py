"""

Дан массив. Переписать его элементы в другой массив такого же размера следующим образом:
    сначала должны идти все отрицательные элементы,
    а затем все остальные.
    Использовать только один проход по массиву.

"""

import random

length = 50
ar = [random.randint(-100, 100) for i in range(length)]
sorted_ar = []

for i in ar:
    if i >= 0: # Здесь 0 -> положительное число (условно)
        sorted_ar.append(i)
    else:
        sorted_ar.insert(0, i)

print(f'Исходный: {ar}')
print(f'Отсортированный: {sorted_ar}')