
# Задание 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(М) конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# оптимальную стратегию можно выразить так:
# Бери столько предметов, чтобы после твоего хода количество предметов было кратно (M+1)
# Тоесть в данном случае нужно взять 20 конфет, 2001 кратно 29

from random import randint


def player_move(player: list, candy: int):
    global total_candy
    player[0] += candy
    total_candy -= candy


# "Интеллект" бота заключается в том что на последнем ходу, если он может забрать остатки, он забирает
def candy_bot(total_candy: int, max_candy_round: int):
    if total_candy > max_candy_round:
        return randint(1, max_candy_round)
    else:
        return total_candy


total_candy = 2021
max_candy_round = 28
first_player = [0]  # Создано листом для передачи в функцию по ссылке
second_player = [0]
motion = 1


print(' На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n \
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n \
Все конфеты оппонента достаются сделавшему последний ход.')
bot_question = input(
    'Вы хотите сыграть с ботом?, если да то введите "да", если нет то введите любой сивол ').lower()
bot_game:bool = True if bot_question == 'да' else False
fate = randint(1, 2)
if bot_game:
    print('Игра - человек против компьютера')
    if fate == 1:  # Жребий на первый ход c ботом
        first_player_name = input('Введите имя - ')
        second_player_name = 'Компьютер'
    else:
        first_player_name = 'Компьютер'
        second_player_name = input('Введите имя - ')
elif fate == 1:  # Жребий на первый ход
    print('Игра - человек против человека')
    first_player_name = input('Введите имя - ')
    second_player_name = input('Введите имя - ')
else:
    print('Игра - человек против человека')
    second_player_name = input('Введите имя - ')
    first_player_name = input('Введите имя - ')
while True:
    print(f'Ход № {motion} \n \
Количество конфет у {first_player_name} = {first_player[0]}\n \
Количество конфет у {second_player_name} = {second_player[0]}')
# Ход первого игрока
    if bot_game and fate == 2:
        first_player_candy = candy_bot(total_candy, max_candy_round)
        print(f'{first_player_name} берёт - {first_player_candy} конфет')
    else:
        while True:
            try:
                first_player_candy = int(input(f'{first_player_name}, возьмите не более \
{max_candy_round if max_candy_round < total_candy else total_candy} конфет - '))
            except ValueError:
                continue
            else:
                if 0 < first_player_candy <= (max_candy_round if max_candy_round < total_candy else total_candy):
                    print(
                        f'{first_player_name} берёт - {first_player_candy} конфет')
                    break
    player_move(first_player, first_player_candy)
    print(f'Осталось конфет - {total_candy}')
    if total_candy <= 0:
        print(f'{first_player_name} победил')
        break

# Ход второго игрока или бота
    if bot_game and fate == 1:
        second_player_candy = candy_bot(total_candy, max_candy_round)
        print(f'{second_player_name} берёт - {second_player_candy} конфет')
    else:
        while True:
            try:
                second_player_candy = int(input(f'{second_player_name}, возьмите не более \
{max_candy_round if max_candy_round < total_candy else total_candy} конфет - '))
            except ValueError:
                continue
            else:
                if 0 < second_player_candy <= (max_candy_round if max_candy_round < total_candy else total_candy):
                    print(
                        f'{second_player_name} берёт берёт - {second_player_candy} конфет')
                    break
    player_move(second_player, second_player_candy)
    print(f'Осталось конфет - {total_candy}')
    motion += 1
    if total_candy <= 0:
        print(f'{second_player_name} игрок победил')
        break
