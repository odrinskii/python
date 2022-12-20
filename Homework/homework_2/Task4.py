# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# data = open('file.txt', 'a')
# info = ['0\n', '3\n', '4\n']
# data.writelines(info)
# data.close()

a = int(input('Введите число: '))
cage = []
for i in range(-a, a + 1):
    cage.append(i)
print(cage)

div = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    div *= cage[int(line)]
data.close()
print(div)

