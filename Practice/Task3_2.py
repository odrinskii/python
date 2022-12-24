# 20. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

cage = ['qwe', 'war', '45', 'raw']
flag = False
for i in cage:
    if i.isnumeric():
        flag = True
        print(f'Числовой элемент найден. Это - {i}')
print(flag)