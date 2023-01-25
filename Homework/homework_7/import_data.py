# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона,
# комментрий - символ разделитель на выбор(можно использовать пробел или запятые)
# + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии
import view
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
    new_name, new_surname = view.get_name()
    data.append(new_name)
    data.append(new_surname)
    new_phone = view.get_phone()
    data.append(new_phone)
    new_comment = view.get_comment()
    data.append(new_comment)
    print(f'Новый контакт: {data}')
    writer_object = writer(add_info)
    writer_object.writerow(data)
    add_info.close()


# new_data(dataset)
