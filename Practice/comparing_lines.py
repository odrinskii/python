one = input()
two = input()
count = 0
for i in range(len(one) - len(two) + 1):  # идём по первой строке, пока не приближаемся к выходу из диапазона
    if one[i:i + len(two)] == two:  # если срез из первой строки, равный длине второй, равен второй строке, то считаем
        count += 1
print(count)