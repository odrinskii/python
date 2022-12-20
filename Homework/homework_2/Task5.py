# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите длину списка: '))
cage = list()
for i in range(n):
    cage.append(random.randrange(-50, 50))
print(f'Исходный список: {cage}')

mixed_cage = cage
length = len(cage)
for i in range(length):
    index_random = random.randint(0, length - 1)
    temp = mixed_cage[i]
    mixed_cage[i] = mixed_cage[index_random]
    mixed_cage[index_random] = temp
print(f'Перемешанный список: {mixed_cage}')


