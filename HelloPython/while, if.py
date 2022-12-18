# задача инвертировать число

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('Хватит')
print(inverted)


for i in 1,2,3,4,5:
    print(i ** 2)

list = [1, 2, 3, 4, 5]
for i in list:
    print(i ** 2)
    
r = range(12)
for i in r:
    print(i)
# либо сразу так

for i in range(10):
    print(i)

# также можно запускать две координаты, например

for i in range(10, 23):
    print(i)

#help(int)


# Вложенный цикл. 
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)