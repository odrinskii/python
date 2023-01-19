# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#
#         b) Подумайте как наделить бота ""интеллектом""
# (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать,
# чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

import random


def pvp():
    player1 = input('Имя первого игрока: ')
    player2 = input('Имя второго игрока: ')
    candies = 221
    candies_per_turn = 28

    first_turn = random.choice([player1, player2])

    current_player = player1 if first_turn == player1 else player2

    while candies > 0:
        print(f'Ходит {current_player}')
        turn = int(input("Введите количество конфет: "))

        while not 0 < turn <= candies_per_turn:
            print("Введите количество конфет от 0 до", candies_per_turn)
            turn = int(input("Введите количество конфет: "))

        candies -= turn
        if candies > 0:
            print(f"Осталось {candies} конфет.")
        else:
            print(f"Осталось {candies} конфет.")

        current_player = player2 if current_player == player1 else player1

    winner = player2 if current_player == player1 else player1
    print(f"Поздравляем победителя - {winner}!!!")


def pve_s():  # бот рандомный
    player1 = input('Имя первого игрока: ')
    player2 = "Bot"
    candies = 221
    candies_per_turn = 28

    first_turn = random.choice([player1, player2])
    current_player = player1 if first_turn == player1 else player2

    while candies > 0:
        print(f'Ходит {current_player}')
        if current_player == player1:
            turn = int(input("Введите количество конфет: "))

            while not 0 < turn <= candies_per_turn:
                print("Введите количество конфет от 0 до", candies_per_turn)
                turn = int(input("Введите количество конфет: "))

            candies -= turn
            if candies > 0:
                print(f"Осталось {candies} конфет.")
            else:
                print(f"Осталось {candies} конфет.")

            current_player = player2 if current_player == player1 else player1
        else:
            turn = random.randint(1, candies_per_turn)
            print(f"Bot взял {turn} конфет.")

            candies -= turn
            if candies > 0:
                print(f"Осталось {candies} конфет.")
            else:
                print(f"Осталось {candies} конфет.")

            current_player = player2 if current_player == player1 else player1


    winner = player2 if current_player == player1 else player1
    print(f"Поздравляем победителя - {winner}!!!")


def pve_smart():  # бот умный
    player1 = input('Имя первого игрока: ')
    print("Второй игрок - Bot")
    player2 = "Bot"
    candies = int(input("Введите общее количество конфет:"))
    candies_per_turn = int(input("Введите максимальное количество конфет за ход:"))

    first_turn = random.choice([player1, player2])
    current_player = player1 if first_turn == player1 else player2

    while candies > 0:
        print(f'Ходит {current_player}')
        if current_player == player1:
            turn = int(input("Введите количество конфет: "))

            while not 0 < turn <= candies_per_turn:
                print("Введите количество конфет от 0 до", candies_per_turn)
                turn = int(input("Введите количество конфет: "))

            candies -= turn
            if candies > 0:
                print(f"Осталось {candies} конфет.")
            else:
                print(f"Осталось {candies} конфет.")

            current_player = player2 if current_player == player1 else player1
        else:
            if candies <= candies_per_turn:
                turn = candies
            elif candies % candies_per_turn == 0:
                turn = candies_per_turn - 1
            else:
                if candies % candies_per_turn == 1:
                    turn = candies_per_turn - 1
                else:
                    turn = candies % candies_per_turn - 1

            print(f"Bot взял {turn} конфет.")

            candies -= turn
            if candies > 0:
                print(f"Осталось {candies} конфет.")
            else:
                print(f"Осталось {candies} конфет.")

            current_player = player2 if current_player == player1 else player1


    winner = player2 if current_player == player1 else player1
    print(f"Поздравляем победителя - {winner}!!!")


pve_smart()