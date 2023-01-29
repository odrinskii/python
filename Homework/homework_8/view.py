def get_name():
    nm = input('Введите имя:')
    return nm


def get_surname():
    s_name = input('Введите фамилию:')
    return s_name


def get_lesson():
    lsn = input('Введите предмет: ')
    return lsn


def get_grade():
    grd = int(input('Введите оценку от 1 до 5: '))
    return grd


def option():
    opt = int(input('Выберите действие: \n'
                    '1 - Добавить студента\n'
                    '2 - Добавить предмет\n'
                    '3 - Добавить оценку\n'
                    '4 - Закрыть программу.\n'))
    while not 1 <= opt <= 4:
        opt = int(input('Ошибка! Введите предложенный номер команды.'))
    return opt


