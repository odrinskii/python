#     Напишите программу, которая принимает на вход координаты двух точек 
#     и находит расстояние между ними в 2D пространстве.

#     Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


a, b = int(input('Введите координаты a:')), int(input('Введите координаты b:'))
c, d = int(input('Введите координаты c:')), int(input('Введите координаты d:'))

length = ((c - a) ** 2 + (d - b) ** 2) ** 0.5

print(f'Расстояние между точками равно: {round(length, 3)}')
