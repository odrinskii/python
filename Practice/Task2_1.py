# 11. Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
# # *Пример:*
# # - Для N = 5: 1, -3, 9, -27, 81
#


# import random
n = int(input('Введите число: '))
cage = list()
a = 1
cage.append(a)
for i in range(1, n):
    a *= -3
    cage.append(a)
print(cage)
