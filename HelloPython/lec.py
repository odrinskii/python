#print('Hello world!')
value = None
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value)
# использование функции type() для выяснения типа переменной
# print(type(a))
# print(type(b))
value = 1234
# print(type(value))

s = 'hello world'
print(s)
# print(type(s))

print(a, '-' ,b, '-', s)
# можно заранее задать формат
print('{} - {} - {}'.format(a,b,s))
# еще вариант
print(f'{a} - {b} - {s}')
# также можно менять порядок вывода с помощью .format() и указания идентификатора
print('{1} - {2} - {0}'.format(a,b,s))

f = False
print(f)

list = [1, 2, 3]
print(list)
list = ['1', '2', '3']
print(list)
list = [True, False]
print(list)


