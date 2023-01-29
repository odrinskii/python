import view
import csv
import ast


def import_data(m_l):
    lists = [view.get_name(), view.get_surname()]
    m_l.append(lists)
    return m_l


def import_lesson(lis):
    lsn = view.get_lesson()
    ls_dict = {lsn: None}
    for item in lis:
        item.append(ls_dict)
    return lis


def import_grade(lis):
    lis_2 = []
    print('Для добавления оценки укажите предмет и данные студента:')
    lesn = view.get_lesson()
    nam = view.get_name()
    sunm = view.get_surname()
    for item in lis:
        if nam in item and sunm in item:
            print('Студент найден!')
            for element in item:
                if '{' in element:
                    element = ast.literal_eval(element)
                lis_2.append(element)
            for element in lis_2:
                if element == {lesn: None}:
                    index = lis_2.index(element)
                    lis_2[index] = {lesn: view.get_grade()}
            item = lis_2
        print('Оценка добавлена')
        print(lis)
        return lis


def load(m_l):
    with open('school.csv', 'w') as file:
        for row in main_list:
            writer_object = csv.writer(file)
            writer_object.writerow(row)


def download(m_l):
    temp = []
    with open('school.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            m_l.append(row)
            temp = []
    return m_l


main_list = []
main_list_2 = []
download(main_list)

opt = view.option()
while not opt == 4:
    if opt == 1:
        import_data(main_list)
    elif opt == 2:
        import_lesson(main_list)
    elif opt == 3:
        import_grade(main_list)
    opt = view.option()

print(main_list)
load(main_list)
