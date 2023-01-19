# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def coding(txt):
    count = 1
    output = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            output += str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):   # проверка на последние
        output += str(count) + txt[-1]
    return output


def decoding(txt):
    number = ''
    output = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():            # isalpha() возвращает True, если в строке только буквы
            number += txt[i]
        else:
            output += txt[i] * int(number)
            number = ''
    return output


data_in = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEEEEEEEE'   # 1122335488888666
print(f'Входные данные: {data_in}')
s = data_in
print(f"Выходные данные: {coding(s)}")
print(f"Данные после декодировки: {decoding(coding(s))}")


# разбор не семинаре
# def encode(data):
#     output = ""
#     prev_item = data[0]
#     count = 0
#     for item in data:
#         if item != prev_item:
#             output += f'{count}{prev_item}'
#             prev_item = item
#             count = 1
#         else:
#             count += 1
#     output += f'{count}{prev_item}'
#     return output
#
#
# def decode(data):
#     output = ''
#     count = ''
#     digit = True
#     for item in data:
#         if digit:
#             count = int(item)
#             digit = False
#         else:
#             output += int(count) * item
#             digit = True
#     return output
#

# print(f'Выходные данные: {encode(data_in)}')
# data_out = encode(data_in)
# data_in = 'AAAAAAFDDCCCCCCCAEEEEEEEE'
# print(f'Входные данные: {data_in}')
# print(f'Новые входные данные: {data_out}')
# print(f'Выходные данные: {decode(data_out)}')