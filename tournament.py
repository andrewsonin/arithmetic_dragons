# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message ='', dragon=''):
    answer = None
    while answer == None:
        if str(type(dragon)).find('Dragon') != -1 or str(type(dragon)).find('Random') != -1:
            try:
                answer = int(input(message))
            except ValueError:
                print('Вы ввели недопустимые символы')
        elif str(type(dragon)).find('Simple') != -1:
            try:
                answer = bool(input(message))
            except ValueError:
                print('Вы ввели недопустимые символы')
        elif str(type(dragon)).find('Mult') != -1:
            try:
                # print(type(input(message)))
                answer = str(input(message))
            except ValueError:
                print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:', dragon)

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
