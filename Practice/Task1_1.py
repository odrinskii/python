# 1. Напишите программу, которая принимает на вход два числа и 
# проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

print('Введите первое и второе число число:')
a, b = int(input()), int(input())

if a != 0 and b != 0:
    if b == a ** 2 or a == b ** 2:
        print('Да')
    else:
        print('Нет')
