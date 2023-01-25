def get_type():
    type = int(input("Введите 1 - комплексные, 0 - действительные "))
    return type

def get_value_int():
    a = int(input("Введи число "))
    b = int(input("Введи число "))
    return a,b

def get_value_complex():
    a = complex(input("Введи число "))
    b = complex(input("Введи число "))
    return a,b

def get_sign(type):
    if type:
        sign = input("Введи знак для комплексных чисел (+,-,/,*) ")
        if sign in ["+","-","/","*"]:
            return sign
        else:
            print("Неверный знак для комплексных чисел ")
    else:
        sign = input("Введи знак для действительных чисел (+,-,/,*,//,%) ")
        if sign in ["+", "-", "/", "*","//","%"]:
            return sign
        else:
            print("Неверный знак для действительных чисел ")

def out(x):
    print(x)
