# 29.Задайте два числа.Напишите программу, которая найдёт НОК(наименьшее общее кратное) этих двух чисел.

a, b = int(input()), int(input())
for i in range(max(a, b), a * b, max(a, b)):
    if i % a == 0 and i % b == 0:
        print(i)
        break

