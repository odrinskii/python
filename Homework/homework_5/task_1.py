# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

data = 'Я не хотабв, а что ты абв, скажешьабв, друг мой?'

data = ' '.join(filter(lambda word: 'абв' not in word, data.split()))
print(data)