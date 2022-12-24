# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.



import datetime

def random_num(max_randon_num):
    random = datetime.datetime.now().microsecond
    print(random)
    return random % max_randon_num

max_random = int(input('Введите максимум для генерации: '))
print(random_num(max_random))


