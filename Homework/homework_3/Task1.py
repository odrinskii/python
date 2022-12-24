# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

cage = []
mysum = 0
print('Введите диапазон и размер случайного списка: ')
m, n, z = int(input('min: ')), int(input('max: ')), int(input('size: '))
for i in range(0, z):
    cage.append(random.randint(m, n))
print(cage)
for i in range(0, z):
    if i % 2 > 0:
        mysum += cage[i]
print(f'Сумма элементов, стоящих на нечетных позициях равна - {mysum}')


