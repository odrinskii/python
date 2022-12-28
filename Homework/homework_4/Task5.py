# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def rep_split(a):

    res = ''
    a = a.replace(' + ', ' +').replace(' - ', ' -')
    a = list(a.split(' '))
    a = a[:-2]
    for i in range(len(a)):
        res = res + str(a[i])
    return res

print('Считываю и вывожу на экран два многочлена из разных файлов: ')
data1 = open('fileHW4_1.txt', 'r')
data2 = open('fileHW4_2.txt', 'r')
mn1, mn2 = str(data1.readline()), str(data2.readline())
print(mn1)
print(mn2)
mn1, mn2 = rep_split(mn1), rep_split(mn2)
result = f'{mn1}+{mn2}=0'
print(f'Результат сложения двух многочленов - {result}')
