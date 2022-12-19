def input_numbers(text_input):
    is_ok = False
    number = None
    while not is_ok: # пока is_ok = False пробуем
        try:
            number = int(input(f"{text_input}"))
            is_ok = True
        except ValueError:
            print('Ошибка! Требуется ввод числа.')
    return number


input_numbers('Введите число: ')