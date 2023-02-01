import datetime
import telebot
from telebot import types

bot = telebot.TeleBot("5915475601:AAHanxUohsp0rsDcW_zwbI81TDhC5vpZoL0")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "/button")  # функция шлет сообщение в бот


@bot.message_handler(commands=["button"])
def button(message):
    # if message.text == "клавиатура":
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # делаем клавиатуру вызова
    but1 = types.KeyboardButton("Сделать предложение")  # делаем кнопку
    but2 = types.KeyboardButton("Узнать время")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выбери опцию: ", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "Сделать предложение":
        bot.send_message(message.chat.id, "Введи имя и фамилию")
        bot.register_next_step_handler(message, sentence)
    elif message.text == "Узнать время":
        bot.send_message(message.chat.id, f"Текущее время - {datetime.datetime.now()}")
        button(message)


def sentence(message):
    text = message.text
    name = text.split()[1]
    surname = text.split()[0]
    bot.send_message(message.chat.id, f"Вас зовут - {name}, фамилия - {surname}")
    button(message)


bot.infinity_polling()  #бесконечная проверка
