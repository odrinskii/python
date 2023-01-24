# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона,
# комментрий - символ разделитель на выбор(можно использовать пробел или запятые)
# + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии
from csv import writer


# dataset = ['id', 'name', 'surname', 'phone number', 'comment']
# with open('contacts.csv', 'w') as addinf:
#     writer_object = writer(addinf)
#     writer_object.writerow(dataset)
# dataset = []


def new_data(data):
    add_info = open("contacts.csv", "a")
    read_info = open("contacts.csv", "r")
    new_id = sum(1 for line in read_info)
    data.append(new_id)
    new_name, new_surname = input("Имя контакта: "), \
        input("Фамилия контакта: ")
    data.append(new_name)
    data.append(new_surname)
    new_phone = input("Введите корректный номер телефона(11 цифр): ")
    while not(new_phone.isnumeric() and len(new_phone) == 11):
        new_phone = input("Введите кооректный номер телефона: ")
    data.append(new_phone)
    new_comment = input("Введите комментарий: ")
    data.append(new_comment)
    print(f'Новый контакт: {data}')
    writer_object = writer(add_info)
    writer_object.writerow(data)
    add_info.close()


# new_data(dataset)
