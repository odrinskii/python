import random

# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

# list_a = [1, 2, 3, 5, 7, 8, 9, 10]
# list_b = [1, 2, 4, 8, 9]
#
# # старая школа
# # print(len(list_new))
# # for i in range(0, len(list_b)):
# #     for j in range(0, len(list_a)):
# #         if list_b[i] == list_a[j]:
# #             list_new.append(list_a[j])
# # print(list_new)
#
# print(list(filter(lambda x: x in list_a, list_b)))   # вот это да!


# 42)Имеется упорядоченный список:
a = [[1, 2, 3],  # 0
     [4, 5, 6],  # 1
     [7, 8, 9]]  # 2
# Перебрать все элементы этого списка с помощью функций enumerate и элементы,
# стоящие на главной диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.
#

# for i, j in enumerate(a):
#     j[i] = 0
# print(a)

# 43) Имеется список id сотрудников из 10 элементов,
# каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)
# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.
# Выведете имена сотрудников, получившие нечетное id.
# Решить с помощью zip,filter,lambda

id_list = random.sample(range(0, 100), 10)
print(id_list)
name_list = ['Andrei', 'Zina', 'Artem', 'Viktor', 'Valya',
             'Igor', 'Andy', 'Kobe', 'Giannis', 'Osel']

union = list(sorted(zip(id_list, name_list)))
print(union)
res = list(filter(lambda x: x[0] % 2 == 1, union))
print(res)
new_name_list = list(map(lambda x: x[1], res))

print(new_name_list)
