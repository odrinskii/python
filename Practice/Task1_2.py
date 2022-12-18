# Напишите программу, которая принимает на вход 5 чисел и находит максимальное из них.

# print('Введите пять чисел:')
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# numbers = [a, b, c, d, e]
# max = a
# for i in numbers:
   
#     if i > max:
#         max = i
# print(max)


# #решение с помощью библиотек
# print('Введите пять чисел:')
# print(max(int(input()), int(input()), int(input()), int(input()), int(input())))

# решение, если идти по индексам
print('Введите пять чисел:')
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
numbers = [a, b, c, d, e]
max = a
for i in range(0, len(numbers)):
   if numbers[i] > max:
     max = numbers[i]
print('Максимальное число - ', max)