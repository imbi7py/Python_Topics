# -*- coding: utf-8 -*-

x = int(input('x = '))

if 0 < x < 7:
    print('Значение x входит в заданный диапазон, продолжаем')
    y = 2 * x - 5
    if y < 0:
        print('Значение y отрицательно')
    else:
        if y > 0:
            print('Значение y положительно')
        else:
            print('y = 0')