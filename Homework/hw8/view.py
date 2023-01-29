def get_option():
    opt = int(input('1 - Добавить студента\n'
                '2 - Добавить предмет\n'
                '3 - Добавить оценку\n'
                '4 - Показать список студентов\n'
                '5 - Показать лист оценок студента\n'
                '6 - Завершить программу\n'))
    return opt

def get_student():
    name = input('Введите имя и фамилию: ')
    return name

def get_lesson():
    lsn = input('Введите предмет:')
    return lsn


def get_grade():
    name = input('Введите имя:')
    lsn = input('Введите предмет:')
    grade = int(input('Введите оценку:'))
    return name, lsn, grade


def get_students_grades():
    name = input('Введите имя студента: ')
    return name

