# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class RandomTroll(Troll):
    def __init__(self):
        self._health = 20
        self._attack = 5
        self._color = 'оранжевый'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(str(d))
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(str(n))
    return Ans


class SimpleTroll(Troll):
    def __init__(self):
        self._health = 20
        self._attack = 5
        self._color = 'серый'

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Простое ли число ' + str(x) + '?. Допустимые варианты ответа: True, False'
        self.set_answer(isPrime(x))
        return self.__quest


class MultiplierTroll(Troll):
    def __init__(self):
        self._health = 20
        self._attack = 5
        self._color = 'розовый'

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Разложите на множители число ' + str(x) + ' и перечислите их через запятую'
        self.set_answer(', '.join(Factor(x)))
        return self.__quest


enemy_types = [MultiplierTroll, GreenDragon, RedDragon, BlackDragon, RandomTroll, SimpleTroll]