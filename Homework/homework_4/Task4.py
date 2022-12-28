# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def rnd_list(m, n, p):
    lst = []
    set_lst = []
    for i in range(p + 1):
        lst.append(random.randint(m, n))
    set_lst = list(set(lst))
    lst = random.sample(set_lst, 3)
    return lst

print('Введите диапазон списка коэффициентов: ')
a, b, z = int(input('Минимальное значение: ')), int(input('Максимальное значение: ')), \
    int(input('Введите размер списка: '))
k = int(input('Введите степень k: '))
new_lst = rnd_list(a, b, z)
a, b, c = new_lst[0], new_lst[1], new_lst[2]
print(f'Список коэффицентов многочлена: {new_lst}')

# data = open('fileHW4.txt', 'a')
data = open('fileHW4.txt', 'w')
if a == 0:
    data.write(f'{b}x + {c} = 0')
elif b == 0:
    data.write(f'{a}x**{k} + {c} = 0')
elif c == 0:
    data.write(f'{a}x**{k} + {b}x = 0')
else:
    data.write(f'{a}x**{k} + {b}x + {c} = 0')
data.close()

print(f'Новый многочлен в степени {k} сформирован и хранится в файле fileHW4.txt!')




