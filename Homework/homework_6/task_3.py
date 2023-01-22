# Задача 32:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def divrecurs(x, y, result):
    if y == 1:
        return result
    return divrecurs(x, y - 1, result * x)


a, b = int(input('Введите первое число: ')), \
    int(input('Введите второе число: '))
res = a
print(f"Результат: {divrecurs(a, b, res)}")




