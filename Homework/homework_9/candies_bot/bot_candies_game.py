import telebot
import random
from telebot import types

bot = telebot.TeleBot("6019861604:AAHkljE2haXdGoyr7LfRSaWNJpXTt7L2zOE")

candies = 221
max_candies = 28
user_turn = 0
bot_turn = 0


@bot.message_handler(commands=["start"])
def launch_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key = types.KeyboardButton("Начать игру.")
    markup.add(key)
    bot.send_message(message.chat.id, "Начнём? ", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def start(message):
    global current_player
    if message.text == "Начать игру.":
        bot.send_message(message.chat.id, "Добро пожаловать в игру!\n"
                                          "Попробуй победить бота!\n"
                                          "\n"
                                          "На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. ")
        bot.send_message(message.chat.id, f"В игре {candies} конфета\n"
                                          f"Максимальное количество конфет за ход - {max_candies}\n")
        current_player = random.choice(["Игрок", "Бот"])
        if current_player == "Игрок":
            bot.send_message(message.chat.id, "Первым ходит Игрок")
            controller(message)
        if current_player == "Бот":
            bot.send_message(message.chat.id, "Первым ходит Бот")
            controller(message)
        # bot.send_message(message.chat.id, "/launch")  # функция шлет сообщение в бот


def controller(message):
    global current_player
    if candies > 0:
        if current_player == "Игрок":
            bot.send_message(message.chat.id, f"Ваш ход! Введите количество конфет от 0 до {max_candies}")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        current_player = "Игрок" if current_player == "Бот" else "Бот"
        bot.send_message(message.chat.id, f"Победил {current_player}")


def user_input(message):
    global current_player, user_turn, candies
    user_turn = message.text
    if user_turn.isdigit():
        user_turn = int(message.text)
        if 0 < user_turn <= max_candies:
            current_player = "Игрок" if current_player == "Бот" else "Бот"
            candies -= user_turn
            bot.send_message(message.chat.id, f"Игрок взял {user_turn} конфет.\n"
                                              f"Осталось {candies} конфет.\n")
            controller(message)
        else:
            bot.send_message(message.chat.id, f"Введено неверное количество конфет!\n")
            controller(message)
    else:
        bot.send_message(message.chat.id, f"Введите число!\n")
        controller(message)


def bot_input(message):
    global candies, bot_turn, current_player
    if candies <= max_candies:
        bot_turn = candies
    elif candies % max_candies == 0:
        bot_turn = max_candies - 1
    else:
        if candies % max_candies == 1:
            bot_turn = max_candies - 1
        else:
            bot_turn = candies % max_candies - 1
    current_player = "Игрок" if current_player == "Бот" else "Бот"
    candies -= bot_turn
    bot.send_message(message.chat.id, f"Бот взял {bot_turn} конфет.\n"
                                      f"Осталось {candies} конфет.\n")
    controller(message)


bot.infinity_polling()
