 # 1)Создайте список из случайных чисел.
 # Найдите максимальное количество его одинаковых элементов.

import random

book = list()
for i in range(11):
    book.append(random.randrange(0, 10))
print(book)
print(set(book))  # делаем из списка множество, чтобы не искать одинаковые элементы каждый раз
cnt = 0
max_digit = 1
for i in set(book):
    cnt = book.count(i)
    if cnt > max_digit:
        max_digit = cnt
print(max_digit)
