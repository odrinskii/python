def get_name():
    new_name, new_surname = input("Имя контакта: "), \
        input("Фамилия контакта: ")
    return new_name, new_surname


def get_phone():
    new_phone = input("Введите корректный номер телефона(11 цифр): ")
    while not (new_phone.isnumeric() and len(new_phone) == 11):
        new_phone = input("Введите корректный номер телефона(11 цифр): ")
    return new_phone


def get_comment():
    new_comment = input("Введите комментарий: ")
    return new_comment


def get_welcome():
    print("Добро пожаловать в телефонный справочник!")
    option = int(input("Выберите действие:\n"
                       "1 - Добавить контакт\n"
                       "2 - Найти контакт по имени\n"
                       "3 - Найти контакт по телефону\n"
                       "4 - Показать все записи\n"
                       "5 - Сортировка по фамилии в алфавитном порядке\n"))
    while not (option == 1 or option == 2 or option == 3 or option == 4
               or option == 5):
        option = input("Ошибка! Введите предложенный номер действия!")
    return option


def get_phonebook():
    import csv
    with open('contacts.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            united_row = ''
            for i in range(len(row)):
                new_row = str(row[i])
                new_row = f'{new_row:<15}'
                united_row += new_row
            print(united_row)


def sort_phonebook():
    import csv
    temp = []
    temp_p = []
    with open('contacts.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            temp.append(row)
        temp_p.extend(temp)
        temp.pop(0)
        sort_temp = sorted(temp, key=lambda x: x[2])
        sort_temp.insert(0, temp_p[0])
        united_row = ''
        for i in range(len(sort_temp)):
            united_row = ''
            # new_row = str(sort_temp[i])
            # new_row = f'{new_row:<15}'
            # print(new_row)
            for j in range(len(sort_temp[i])):
                new_row = str(sort_temp[i][j])
                new_row = f'{new_row:<15}'
                united_row += new_row
            print(united_row)

