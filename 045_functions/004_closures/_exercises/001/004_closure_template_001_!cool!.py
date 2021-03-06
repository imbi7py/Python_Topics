# -*- coding: utf-8 -*-

# # В питоне циклы не создают область видимости, что делает создание замыканий несколько нетривиальным.
# #
# # Простой пример: в массив multipliers мы размещаем функции, которые умножают аргумент на 0, 1, 2, 3, 4
#
# multipliers _    # list
# ___ m __ r.. 5
#     ?.ap.. l___ x x * m
#
# print ? i 5 ___ i __ r.. 5
#
# # [20, 20, 20, 20, 20]
#
# # На самом деле, все функции будут умножать аргумент на 4, на выходе мы получим [20, 20, 20, 20, 20].
# # Чтобы получить правильные замыкания, гайды рекомендуют делать так:
#
# multipliers      # list
#
# ___ m __ r.. 5
#     ?.ap.. l___ x real_m _ m x * ?
#
# print ? i 5 ___ ? __ r.. 5
# # [0, 5, 10, 15, 20]
#
# # В этом случае m биндится сразу, т. к. находится не в теле функции. Если вам кажется, что это похоже на хак,
# # то вы правы. Такой подход ломает интерфейс функции, оставляя возможность указывать real_m снаружи,
# # что достаточно криво. Но все становится еще хуже, если вы хотите вместо x использовать *args.
#
# multipliers     # list
#
# ___ m __ r.. 5
#     ?.ap.. l___ $ x * m ___ x i_ a..
#
# print ? i 1, 2, 3 ___ i __ r.. 5
# # [[4, 8, 12], [4, 8, 12], [4, 8, 12], [4, 8, 12], [4, 8, 12]]
#
# # это синтаксически неверно,
# # нельзя ставить параметр после *args
# # multipliers.ap..(l___ *args, real_m=m: [x * real_m ___ x i_ args])
#
# # Как еще можно решить эту проблему, не прибегая к хаку с дефолтным значением аргумента? Нужно сделать так,
# # чтобы значение m рельно использовалось в цикле, а не просто прокидывалось в тело функции.
# # Для этого используем его в качестве аргумента промежуточной функции:
# # partial создает функцию-обертку, позволяя задать заранее некоторые дефолтные значения параметров.
# # Правда, с partial конкретно в моем случае возникла неожиданная проблема:
# # она возвращает вызываемый functools.partial object, но не обычную функцию, что почему-то не устраивает библиотеку,
# # с который я работаю.
#
# multipliers        # list
#
# ___ m __ r.. 5
#     ___ _closure m
#         r_ l___ $ x * ? ___ ? __ a..
#
#
#     ?.ap.. _c.. m
#
# print ? i 1, 2, 3 ___ i __ r.. 5
# # [[0, 0, 0], [1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]]
#
# # Более того, функция подобная _closure уже есть в стандартной библиотеке:
# ____ f... _______ pa...
#
# multipliers     # list
#
#
# ___ mult_array m, $
#     r_ x*? ___ ? __ a...
#
# ___ m __ r.. 5
#     ?.ap.. pa... m.., ?
#
# print ? i 1, 2, 3 ___ ? __ r.. 5
# # [[0, 0, 0], [1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]]
