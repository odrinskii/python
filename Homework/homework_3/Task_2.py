# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random


def new_int_list(arr):
    print('Введите диапазон и размер случайного списка: ')
    m, n, z = int(input('min: ')), int(input('max: ')), int(input('size: '))
    for item in range(0, z):
        arr.append(random.randint(m, n))
    print(arr)


cage = []
new_int_list(cage)
my_sum = 0
new_cage = []
for i in range(len(cage) // 2):
    my_sum = cage[i] * cage[len(cage) - 1 - i]
    new_cage.append(my_sum)
if len(cage) % 2 != 0:
    new_cage.append(cage[len(cage) // 2] ** 2)
print(new_cage)
