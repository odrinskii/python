# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# # # 1) с помощью математических формул нахождения корней квадратного уравнения
# # # 2) с помощью дополнительных библиотек Python
import math


a, b, c = int(input()), int(input()), int(input())
x1, x2 = 0, 0
d = (b ** 2) - (4 * a * c)
if d > 0:
    print(f'Дискриминант больше нуля - {d}')
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'Корни уравнения: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}')
elif d == 0:
    print('Дискриминант равен нулю.')
    x1 = -b / 2 * a
    print(f'Корень уравнения один и равен {round(x1, 2)}')
else:
    print('Корней нет.')
