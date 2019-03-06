# -*- coding: utf-8 -*-
import random
from Slovar import *


vopros = False
otvet = False
prosba = False
privet = False
poka = False

def open_file():
    bd = {}

    key = ''
    val = ''

    keys = []
    vals = []

    f = open('text_ru.txt', 'rt', encoding='utf-8')
    for line in f:
        l = line.strip()

        if l[0] == '0':
            key = l[2::].lower()
            keys.append(key)
            vals = []

            if len(keys) > 0:
                bd[key] = vals
                keys = []

        if l[0] == '1':
            val = l[2::]  #.lower()
            vals.append(val)

    f.close()
    return bd


def write_file(bd):
    f = open('text_ru.txt', 'wt', encoding='utf-8')
    for k in bd.keys():
        keys = "0 " + str(k) + '\n'
        f.write(keys)
        for v in bd[k]:
            value = "1 " + str(v) + '\n'
            f.write(value)
    f.close()


def razbor(ask):
    # Захват знака припинания
    znak = ask[-1]
    # Разбиение по словам
    ask_list_edite = []
    ask_list = ask.split(' ')
    for i in ask_list:
        ask_list_edite.append(i.strip(',').strip('.').strip('!').strip('?').strip(' '))

    form(ask_list_edite, znak)
#     Привет, как твои дела?

def form(list, znak):
    vopros = True
    otvet = False
    prosba = False
    privet = False
    poka = False

    for i in voprosi:
        if i in list or znak == '?':
            vopros = True

    for i in priveti:
        if i in list:
            privet = True

    # print('vopros', vopros, '\n', 'otvet', otvet, '\n', 'prosba', prosba, '\n', 'privet', privet, '\n', 'poka', poka)


def speak():
    ask = ''
    bd = open_file()
    while ask != 'пока':
        say = ''
        ask = str(input('Говорите ************** \n')).lower()
        # Шаблонные выражения
        for i in bd:
            if i == ask:
                say = bd[i][random.randint(0, len(bd[i])-1)]
                break

        # Разбор выражения пользователя
        razbor(ask)


        # else:
        #     print('Не понятно, укажите возможный ответ!\n')
        #     new = str(input())  # .lower()
        #     key = ask
        #
        #     bd[key] = (new, )
        #     write_file(bd)

        if say == '':
            print('Не молчи! \n')

        print(say)

speak()