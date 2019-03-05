# -*- coding: utf-8 -*-
import random


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
            if len(keys) > 0:
                bd[key] = vals
                keys = []

            key = l[2::].lower()
            keys.append(key)
            vals = []

        if l[0] == '1':
            val = l[2::]  #.lower()
            vals.append(val)

    f.close()


    return bd

def write_file(bd):
    f = open('text_ru.txt', 'wt', encoding='utf-8')
    f.write(str(bd))
    f.close()

def speak():
    ask = ''
    bd = open_file()
    while ask != 'пока':
        say = ''
        ask = str(input('Говорите ************** \n')).lower()
        for i in bd:
            if i == ask:
                say = bd[i][random.randint(0, len(bd[i])-1)]
        if say == '':
            print('Не понятно, укажите возможный ответ!\n')
            new = str(input())  #.lower()
            key = ask

            bd[key] = (new,)
            write_file(bd)

        print(bd)
        print(say)

# open_file()
speak()