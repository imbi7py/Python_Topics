# # coding: utf-8
#
# """
# Интерпретатор (Interpreter) - паттерн поведения классов.
#
# Для заданного языка определяет представление его грамматики,
# а также интерпретатор предложений этого языка.
# """
#
#
# c_ RomanNumeralInterpreter o..
#     """Интерпретатор римских цифр"""
#     ___ -
#         grammar _ |
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         |
#
#     ___ interpret text
#         numbers _ ma. g__.ge. ?  # строки в значения
#         __ N... _ ?
#             r_ V... ('Ошибочное значение: @'  ?
#         result _ 0  # накапливаем результат
#         temp _ N..  # запоминаем последнее значение
#         w____ ?
#             num _ ?.po. 0
#             __ te.. __ N... o. te.. >_ nu.
#                 re.. +_ nu.
#             ____
#                 r... +_ (n.. - t.. * 2)
#             temp _ nu.
#         r_ r...
#
#
# interp _ R..
# print ?.i...('MMMCMXCIX') == 3999  # True
# print ?.i...('MCMLXXXVIII') == 1988  # True
