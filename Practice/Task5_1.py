# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

# a = [1, 2, 3, 4, 6, 7, 8]
#
# for i in range(1, len(a)):
#     if a[i]-1 != a[i-1]:
#         print(a[i]-1)
#
# 36.Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Строить последовательность начиная с первого элемента, если последовательность построить невозможно,
# начинать со следующего элемента и т.д.
# [1, 5, 2, 3, 4, 6, 1, 7] = [1,5,7]
# [7,5,2,3,4,6,7] = [5,6,7]
# [7,7,2,3,4,6,7] = [2,3,4,6,7]


def posled(data):
    result = []
    flag = False
    length = len(data)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if data[j] > data[i]:
                flag = True
                begin = i
                next = j
                break
        if flag:
            break
    if flag:
        result.append(data[begin])
        result.append(data[next])
        for i in range(next + 1, length):
            if data[i] > result[-1]:
                result.append(data[i])
        return result
    else:
        return -1


data = [7, 5, 2, 3, 4, 6, 7]
data_posled = posled(data)
print(data_posled)


# 37.Напишите программу, удаляющую из текста все слова, содержащие "абв".

# data = 'Я не хотабв, а что ты абв, скажешьабв?'
#
# data = ' '.join(filter(lambda word: not 'абв' in word, data.split()))
# print(data)