# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

a = int(input('Введите число: '))
d = {}
sum = 0
for i in range(1, a + 1):
    d[i] = round((1 + 1 / i) ** i, 2)
    sum += d[i]
print(d)
print(sum)
