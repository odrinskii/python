import view
import modul

def start():
    type = view.get_type()
    if type:
        a,b = view.get_value_complex()
    else:
        a,b = view.get_value_int()
    sign = view.get_sign(type)
    modul.init(a,b)
    res = "ошибка ввода"
    if sign == "+":
        res = modul.summ()
    elif sign == "-":
        res = modul.diff()
    elif sign == "*":
        res = modul.multi()
    elif sign == "/":
        res = modul.div()
    elif sign == "//":
        res = modul.div_cel()
    elif sign == "%":
        res = modul.div_ost()
    view.out(res)






