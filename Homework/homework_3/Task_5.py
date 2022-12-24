# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

cage = []
a = int(input('Введите число: '))
for i in range(a + 1):
    if i == 0:
        cage.append(0)
    elif i == 1:
        cage.append(1)
        cage.insert(0, 1)
    else:
        cage.append(cage[-1] + cage[-2])
        cage.insert(0, cage[1] - cage[0])
print(cage)
