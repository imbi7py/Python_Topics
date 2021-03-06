﻿# # -*- coding: utf-8 -*-
#
# """Обзор операций со словарями"""
#
# phonebook = {
#     'Jack': '032-846',
#     'Guido': '917-333',
#     'Mario': '120-422',
#     'Mary': '890-532',  # последняя запятая игнорируется
# }
#
# # len(d) – количество элементов.
# print ? ?  'entries found')
#
# print()
#
# # d[key] – получение значения с ключом key. Если такой ключ не существует
# # и отображение реализует специальный метод __missing__(self, key), то он
# # вызывается. Если ключ не существует и метод __missing__ не определён,
# # выбрасывается исключение KeyError.
# t__
#     print('Mary:', ? Mary
#     print('Lumberjack:', ? Lumberjack
# ____ K... __ e
#     print('No entry for', $?.a..
#
# print()
#
# # d[key] = value – изменить значение или создать новую пару ключ-значение, если
# # ключ не существует.
# ? Lumberjack = '000-777'
#
# # key in d, key not in d – проверка наличия ключа в отображении.
# ____ person __ 'Guido', 'Mary', 'Ahmed'
#     __ ? __ p..
#         print ? is in the phonebook
#     ___
#         print('No entry found for', ?
#
# print()
#
# # iter(d) – то же самое, что iter(d.keys()).
# print('People in the phonebook:')
# ___ person __ ph..
#     print ?
#
# print()
#
# # copy() – создать неполную копию словаря.
# phonebook_copy = ph__.?
# print('Phonebook:', ph__
# print('Phonebook copy:', p_c
#
# print()
#
# # clear() – удалить все элементы словаря.
# ph_c_.?
# print('Phonebook:', ph..
# print('Phonebook copy:', p_c..
#
# print()
#
# # (метод класса) dict.fromkeys(sequence[, value]) – создаёт новый словарь с
# # ключами из последовательности sequence и заданным значением (по умолчанию –
# # None).
# numbers_dict _ di__.? ra.. 3) 42
# print ?
#
# print()
#
# # d.get(key[, default]) – безопасное получение значения по ключу (никогда не
# # выбрасывает KeyError).  Если ключ не найден, возвращается значение default
# # (по-умолчанию – None).
# ___ key __ ra.. 5
#     print '@:'.f.. ?, n__.? ? 0
#
# print()
#
# # d.items() – в Python 3 возвращает объект представления словаря,
# # соответствующий парам (двухэлементным кортежам) вида (ключ, значение).  В
# # Python 2 возвращает соответствующий список, а метод iteritems() возвращает
# # итератор.  Аналогичный метод в Python 2.7 – viewitems().
# print('Items:', ph__.?
#
# # d.keys() – в Python 3 возвращает объект представления словаря,
# # соответствующий ключам словаря.  В Python 2 возвращает соответствующий
# # список, а метод iterkeys() возвращает итератор.  Аналогичный метод в Python
# # 2.7 – viewkeys().
# print('Keys:', ph__.?
#
# # d.values() – в Python 3 возвращает объект представления словаря,
# # соответствующий значениям.  В Python 2 возвращает соответствующий список, а
# # метод itervalues() возвращает итератор.  Аналогичный метод в Python 2.7 –
# # viewvalues().
# print('Values:', ph__.?
#
# print()
#
# # d.pop(key[, default]) – если ключ key существует, удаляет элемент из словаря
# # и возвращает его значение.  Если ключ не существует и задано значение
# # default, возвращается данное значение, иначе выбрасывается исключение
# # KeyError.
# number = ph__.? Lumberjack
# print('Deleted Lumberjack (was ' + ? + ')')
# print ph__
#
# print()
#
# # d.popitem() – удаляет произвольную пару ключ-значение и возвращает её.  Если
# # словарь пустой, возникает исключение KeyError.  Метод полезен для алгоритмов,
# # которые обходят словарь, удаляя уже обработанные значения (например,
# # определённые алгоритмы, связанные с теорией графов).
# person _ ph__.?
# print('Popped @ (phone: @)'.f.. $?
#
# print()
#
# # d.setdefault(key[, default]) – если ключ key существует, возвращает
# # соответствующее значение.  Иначе создаёт элемент с ключом key и значением
# # default.  default по умолчанию равен None.
# ___ person __ 'Jack', 'Liz'
#     phone _ ph__.? ? 000-000
#     print('@: @'.f..  ? ph..
#
# print ph..
#
# print()
#
# # d.update(mapping) – принимает либо другой словарь или отображение, либо
# # итерабельный объект, состоящий из итерабельных объектов – пар ключ-значение,
# # либо именованные аргументы.  Добавляет соответствующие элементы в словарь,
# # перезаписывая элементы с существующими ключами.
# ph__.? Alex 832-438 Alice 231-987
# ph__.? Joe , 217-531 |  James , 783-428
# ph__.? Carl _ 783-923  Victoria _ 386-486
# print ?
