# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# cage = []
# a = int(input('Введите число: '))
# for i in range(a + 1):
#     if i == 0:
#         cage.append(0)
#     elif i == 1:
#         cage.append(1)
#         cage.insert(0, 1)
#     else:
#         cage.append(cage[-1] + cage[-2])
#         cage.insert(0, cage[1] - cage[0])
# print(cage)

def pos_fib(n):
    pos_list = [0, 1]
    for i in range(n - 1):
        pos_list.append(pos_list[-2] + pos_list[-1])
    return pos_list


def neg_fib(n):
    neg_list = [0, 1]
    for i in range(n - 1):
        neg_list.append(neg_list[-2] - neg_list[-1])
    return neg_list


print(neg_fib(8)[::-1] + pos_fib(8)[1:])


