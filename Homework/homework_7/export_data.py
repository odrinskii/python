def get_search_name():
    search_name = input("Введите свой запрос: ")
    return search_name


def find_data(text):
    import csv
    with open('contacts.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            united_row = " ".join(row)
            if text in united_row:
                print("Найдены совпадения!")
                return print(united_row)
        print("Данные не найдены. ")


def find_data_by_number(text):
    import csv
    with open('contacts.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            united_row = " ".join(row)
            if text in united_row:
                print("Найдены совпадения!")
                return print(str(row[1]) + ' ' + str(row[2]))
        print("Данные не найдены. ")



# with open('contacts.csv', encoding='utf-8') as file:
#     file_reader = csv.reader(file)
#     for row in file_reader:
#         united_row = " ".join(row)
#         print(united_row)