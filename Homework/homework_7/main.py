from import_data import new_data

contact_line = []
print("Добро пожаловать в телефонный справочник!")

option = int(input("Выберите действие:\n"
               "1 - Добавить контакт\n"
               "2 - Найти контакт\n"))

while not (option == 1 or option == 2):
    option = input("Ошибка! Введите предложенный номер действия!")

if option == 1:
    new_data(contact_line)
else:
    print("Модуль в разработке.")
