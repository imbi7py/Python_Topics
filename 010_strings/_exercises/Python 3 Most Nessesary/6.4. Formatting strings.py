# # -*- coding: utf-8 -*-
#
# print("_" _ 10                         # Один элемент
# # '10'
# print("_ — _ — _" _ (10, 20, 30))     # Несколько элементов
# '10 — 20 — 30'
#
#
# print("_ name _ — _ year _" _ "year" 1978 "name" "Nik"     # dict
# # 'Nik — 1978'
#
#
# print("_|_ _|_ _|_" _ 0o77, 10, 105    # oct
# # 0o77 0o12 0o12
# print("_|_ _|_ _|_" _ 0xff, 10, 105    #  hexadecimal
# # 0xff 0xa 0xa
# print("_|_ _|_ _|_" _ 0xff, 10, 105    # hexadecimal with big O
# # 0XFF 0XA 0XA
# print("_|.0F _.0F" _ 300, 300          # tochnost' # для вещественных чисел предписывает всегда выводить дробную
#                                          точку, даже если задано значение о в параметре
# <Точность>:
# # 300. 300
#
""""
о -
"""
# задает наличие ведущих нулей для числового значения:
# print("'_d' — '_##_'" _ 3, 3  # 5 — ширина поля | digit
# # "'3' — '00003'"
#
# - - задает выравнивание по левой границе области. По умолчанию используется
# выравнивание по правой границе. Если флаг указан одновременно с флагом о, то
# действие флага о будет отменено.
# print("'_##' — '_|##'" _ (3, 3))  # 5 — ширина поля | digit
# # "'    3' — '3    '"
# print("'_##' — '_|##'" _ (3, 3))   # 5 — ширина поля | digit
# # "'00003' — '3    '"
#
# пробел - вставляет пробел перед положительным числом. Перед отрицательным
# числом будет стоять минус. Пример:
# print("'_ _' — '_ '" _ (-3, 3))           # | digit
# # "'-3' — ' 3'"
#
"""
+ - 
"""
# задает обязательный вывод знака как для отрицательных, так и для положительных чисел. Если флаг + указан
# одновременно с флагом пробел, то действие флага
# пробел будет отменено.
# print("'_|_' — '_|_'" _ (-3, 3))          # | digit
# # "'-3' — '+3'"
#
#  <Ширина> - мmmмалъная ширина поля. Если строка не помещается в указанную ширину, то значение игнорируется,
#  и строка выводится полностью:
# print("'_10_' — '_-10_'" _ (3, 3))        # | digit
# # "'         3' — '3         '"
# print("'_3_''_10_'" _ ("string", "string"))
# # "'string''    string'"
#
#  Вместо значения можно указать символ "* ". В этом случае значение следует задать внутри кортежа:
# print("'_|_''_10_'" _ (10, "string", "str"))
# # "'    string''       str'"
#
# <Точность> - количество знаков после точки для вещественных чисел. Перед этим параметром обязательно должна стоять
# точка.
# _______ ma__
# print("_ _? _.2_" _ ma__.pi, ma__.pi, ma__.pi))      |float
# # '3.141592653589793 3.141593 3.14'
#
#  Вместо значения можно указать символ «*». В этом случае значение следует задать внутри кортежа:
# print("'_|.|?'" _ (8, 5, ma__.pi))
# # "' 3.14159'"
#
"""
s - 
"""
# преобразует любой объект в строку с помощью функции str () :
# print("_?" _ ("Обычная строка"))
# # Обычная строка
# print("_? _? _?" _ (10, 10.52, [1, 2, 3]))
# # 10 10.52 [1, 2, 3]
#
"""
r - 
"""
# преобразует любой объект в строку с помощью функции repr ( )
# print("_?" _ ("Обычная строка"))
# # 'Обычная строка'
#
"""
 а - 
"""
# преобразует объект в строку с помощью функции ascii ( >:
# print("_?" _ ("строка"))
# # '\u0441\u0442\u0440\u043e\u043a\u0430'
#
"""
с - 
"""
# выводит одиночный символ или преобразует числовое значение в символ. В качестве примера выведем числовое значение
# и соответствующий этому значенmо символ:
# ___ i i_ ra.. 33, 127
#   print("_? => _?" _ ? ?    |string
#
"""
d и i - 
"""
# возвращают целую часть числа:
# print("_? _? _?" _ (10, 25.6, -80))
# # 10 25 -80
# print("_? _? _?" _ (10, 25.6, -80))
# # 10 25 -80
#
"""
о - 
"""
# восьмеричное значение:
# print("_ _ _" _ (0o77, 10, 105))
# # 77 12 12
# print("_#_ _#_ _#_" _ (0o77, 10, 105))
# # 0o77 0o12 0o12
#
"""
х - 
"""
# шестнадцатеричное значение в нижнем регистре:
# print("_ _ _" _ (0xff, 10, 105))
# # ff a a
# print("_# _# _#" _ (0xff, 10, 105))
# # 0xff 0xa 0xa
#
"""
х - 
"""
# шестнадцатеричное значение в верхнем регистре:
# print("_ _ _" _ (0xff, 10, 105))
# # FF A A
# print("_#_ _#_ _#_" _ (0xff, 10, 105))
# # 0XFF 0XA 0XA
#
"""
f и F - 
"""
# вещественное число в десятичном представлении:
# print("_ _ _" _ (300, 18.65781452, -12.5))
# # 300.000000 18.657815 -12.500000
# print("_ _ _" _ (300, 18.65781452, -12.5))
# # 300.000000 18.657815 -12.500000
# print("_#.0_ _.0_" _ (300, 300))
# # 300. 300
#
"""
е - 
"""
# вещественное число в экспоненциальной форме
# print("_ _" _ (3000, 18657.81452))
# # 3.000000e+03 1.865781e+04
#
"""
Е- 
"""
# вещественное число в экспоненциальной форме
# print("_ _" _ (3000, 18657.81452))
# # 3.000000E+03 1.865781E+04
#
"""
g - 
"""
# эквивалентно f или е (выбирается более короткая запись числа):
# print("_ _ _" _ (0.086578, 0.000086578, 1.865E-005))
# # 0.086578 8.6578e-05 1.865e-05
#
# print("_ _ _" _ (0.086578, 0.000086578, 1.865E-005))
# # 0.086578 8.6578E-05 1.865E-05
#
"""
G - 
"""
# эквивалентно f или Е (выбирается более короткая запись числа):
# # print("_ _" _ ("- это символ процента")) # Ошибка
# # Traceback (most recent call last):
# #   File "<pyshell#55>", line 1, in <module>
# #     print("_ _" _ ("- это символ процента")) # Ошибка
# # TypeError: not all arguments converted during string formatting
# print("__ _" _ ("- это символ процента")) # Нормально
# # _ — это символ процента
