# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def new_list(arr):
    print('Введите диапазон и размер случайного списка: ')
    m, n, z = int(input('min: ')), int(input('max: ')), int(input('size: '))
    for item in range(0, z):
        arr.append(round(random.uniform(m, n), 2))
    print(arr)


cage = []
new_cage = []
new_list(cage)
for i in cage:
    i = str(i)
    a = i.split('.')
    new_cage.append(int(a[1]))
set_cage = set(new_cage)
for i in set_cage:
    if i == 0:
        set_cage.remove(i)
        break
print(sorted(set_cage))

result = max(set_cage) - min(set_cage)
print(f'Разница между максимальным и минимальным значением дробной части элементов => {result}')


