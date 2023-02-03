import telebot
from telebot import types
import log
import modul


def main():
    bot = telebot.TeleBot("6049326953:AAGXDwkSM0nZlsUC7DsjKeqEIvAIR-JGyzw")

    @bot.message_handler(commands=["start"])
    def launch_game(message):
        bot.send_message(message.chat.id, "/launch")

    @bot.message_handler(commands=["launch"])
    def button(message):
        log.log(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("Рациональные числа")
        but2 = types.KeyboardButton("Комплексные числа")
        markup.add(but1)
        markup.add(but2)
        bot.send_message(message.chat.id, "Загрузка...", reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def controller(message):
        log.log(message)
        print(message.text)
        if message.text == "Рациональные числа":
            bot.send_message(message.chat.id, "Введите вычисляемое выражение для действительных чисел (+,-,/,*,//,%) через пробел:")
            bot.register_next_step_handler(message, int_numbers)
        if message.text == "Комплексные числа":
            bot.send_message(message.chat.id, "Введите вычисляемое выражение для комплексных чисел (+,-,/,*) через пробел: ")
            bot.register_next_step_handler(message, comp_number)

    def int_numbers(message):
        data_in = message.text.split()
        if len(data_in) < 3:
            bot.send_message(message.chat.id, "Ошибка ввода!")
            log.log(message)
            button(message)
        else:
            sign = data_in[1]
            a = int(data_in[0])
            b = int(data_in[2])
            modul.init(a, b)
            res = "Ошибка ввода"
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
            else:
                bot.send_message(message.chat.id, "Ошибка ввода!")
                log.log(message)
                button(message)
            bot.send_message(message.chat.id, f"{a} {sign} {b} = {res}")
            log.log(message)
            button(message)

    def comp_number(message):
        data_in = message.text.split()
        if len(data_in) < 3:
            bot.send_message(message.chat.id, "Ошибка ввода!")
            log.log(message)
            button(message)
        else:
            sign = data_in[1]
            a = complex(data_in[0])
            b = complex(data_in[2])
            modul.init(a, b)
            res = "Ошибка ввода"
            if sign == "+":
                res = modul.summ()
            elif sign == "-":
                res = modul.diff()
            elif sign == "*":
                res = modul.multi()
            elif sign == "/":
                res = modul.div()
            else:
                bot.send_message(message.chat.id, "Ошибка ввода!")
                log.log(message)
                button(message)
            bot.send_message(message.chat.id, f"{a} {sign} {b} = {res}")
            button(message)

    bot.infinity_polling()
