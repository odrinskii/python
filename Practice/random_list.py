import random
n = int(input('Введите число: '))
cage = list()
for i in range(n):
    cage.append(random.randrange(-50, 50))
print(cage)