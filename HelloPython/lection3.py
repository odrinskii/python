# # def f(x):
# #     return x ** 2
# # #
# # g = f
# #
# # print(type(f))
# # print(type(g))
# #
# # print(f(4))
# # print(g(4))
# #
# # def calc1(x):
# #     return x + 10
# # def calc2(x):
# #     return x * 10
# # def math(op, x):
# #     print(op(x))
# #
# # math(calc2, 10) # работает
# # math(calc1, 10)
#
# # теперь пробуем с двумя переменными
#
# # def sum(x, y):
# #     return x + y
#
# def mult(x, y):
#     return x * y
#
# def calc(op, a, b):
#     print(op(a, b))
#
# calc(mult, 4, 5)
#
# # как можно сделать красивее?
#
# # def sum(x, y):
# #     return x + y
# # это тоже самое, что
#
# sum = lambda x, y: x + y
#
# # также можно не присваивать переменную, а сразу указывать lambda в функции
#
# calc(sum, 4, 5)
# calc(lambda x, y: x + y + 5, 4, 5)
# # 9
# # 14
#
# # LIST COMPREHENSION быстрое создание списков
# # обычно мы делаем так:
#
# list1 = []
#
# for i in range(1, 21):
#     if i % 2 == 0:
#         list1.append(i)
#
# list2 = [i for i in range(1, 21) if i % 2 == 0]  # должно получится тоже самое
#
# print(list1)
# print(list2)
#
# list3 = [(i, i) for i in range(1, 21) if i % 2 == 0]  # можно создавать с кортежами и другими типами данных
#
# print(list3)
#
# list4 = [f(i) for i in range(1, 21) if i % 2 == 0]  # можем в качестве exp указать функцию
# # в таком случае сначала создается список, далее каждый элемент идет на расчет в функцию
# print(list4)
#
# list4 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # ну и также можем использовать кортеж, чтобы показать i и рядом его
# # квадрат
#
# print(list4)
# #

# MAP
# li = [x for x in range(1, 20)]
# print(li)
# li = list(map(lambda x: x + 10, li))
# print(li)


#  FILTER
# data = [x for x in range(10)]
# print(data)
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)


# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

file = open('file.txt', 'r')
data = file.read()
file.close()
print(data.split())

def select(f, col):  # вручную созданный map
    return[f(x) for x in col]

def where(f, col):  # вручную созданный filter
    return [x for x in col if f(x)]

new_data = data.split()

res = map(int, new_data)
print(res)
res = filter(lambda x: not x % 2, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)