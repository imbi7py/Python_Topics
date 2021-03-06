# # -*- coding: utf-8 -*-
#
# d1, d2 = {"a": 1, "b": 2 }, {"a": 3, "c": 4, "d": 5}
# print(d1.? , d2.?                                       # Получаем объект dict_keys
# # (dict_keys(['a', 'b']), dict_keys(['a', 'c', 'd']))
# print(li.. _1.? , li.. _2.?                          # Получаем список ключей
# # (['a', 'b'], ['a', 'c', 'd'])
# ___ k __ _1.?
#   print(?, ..._" ")
#
# # a b
# print(_1.? @ _2.?                                    # Объединение
# # {'a', 'c', 'b', 'd'}
# print(_1.? @ _2.?                                     # Разница
# # {'b'}
# print(_2.? @ _1.?                                    # Разница
# # {'c', 'd'}
# print(_1.? @ _2.?                                     # Одинаковые ключи
# # {'a'}
# print(_1.? @ _2.?                                      # Уникальные ключи
# # {'c', 'b', 'd'}
#
#
# d = {"a": 1, "b": 2}
# print ?.?                                                # Получаем объект dict_values
# # dict_values([1, 2])
# print li.. ?.?                                           # Получаем список значений
# # [1, 2]
# print v ___ ? __ ?.?
# # [1, 2]
#
#
# d = a 1 b 2
# print ?.?                                                  # Получаем объект dict_items
# # dict_items([('a', 1), ('b', 2)])
# print li.. ?.?                                            # Получаем список кортежей
# # [('a', 1), ('b', 2)]
#
#
# d = a 1 b 2
# print("a" in d)                                                   # Ключ существует
# # True
# print("c" in d)                                                   # Ключ не существует
# # False
#
#
# d = {"a": 1, "b": 2}
# print("c" not in d)                                               # Ключ не существует
# # True
# print("a" not in d)                                               # Ключ существует
# # False
#
#
# d = {"a": 1, "b": 2}
# print(?.g.. a ?.g.. c ?.g.. c 800
# # (1, None, 800)
#
#
# d = {"a": 1, "b": 2}
# print(?.s_d_ a ?.s_d_ c ?.s_d_ d, 0
# # (1, None, 0)
# print()
# print(d)
# # {'a': 1, 'c': None, 'b': 2, 'd': 0}
#
#
# d = {"a": 1, "b": 2, "c": 3}
# print(?.p.. a" ?.p.. n" 0
# # (1, 0)print(
# # d.pop("n") # Ключ отсутствует и нет второго параметра)
# # Traceback (most recent call last):
# #   File "<pyshell#40>", line 1, in <module>
# #     d.pop("n") # Ключ отсутствует и нет второго параметра
# # KeyError: 'n'
# print(d)
# # {'c': 3, 'b': 2}
#
#
# d = {"a": 1, "b": 2}
# print ?.p_i_                                                # Удаляем произвольный элемент
# # ('a', 1)
# print ?.p_i_                                                # Удаляем произвольный элемент
# # ('b', 2)
# # d.popitem() # Словарь пустой. Возбуждается исключение
# # Traceback (most recent call last):
# #   File "<pyshell#45>", line 1, in <module>
# #     d.popitem() # Словарь пустой. Возбуждается исключение
# # KeyError: 'popitem(): dictionary is empty'
#
#
# d = a 1 b 2
# ?.?                                                       # Удаляем все элементы
# print(d)                                                         # Словарь теперь пустой
# # {}
#
#
# d = a 1 b 2
# ?.up.. c_3 d_4
# print(d)
# # {'a': 1, 'c': 3, 'b': 2, 'd': 4}
# ?.? c 10 d 20                                     # Словарь
# print(d)                                                         # Значения элементов перезаписаны
# # {'a': 1, 'c': 10, 'b': 2, 'd': 20}
# ?.? d 80 e 6                                  # Список кортежей
# print(d)
# # {'a': 1, 'c': 10, 'b': 2, 'e': 6, 'd': 80}
# ?.? a str|, i t                             # Список списков
# print(d)
# # {'a': 'str', 'c': 10, 'b': 2, 'e': 6, 'd': 80, 'i': 't'}
#
#
# d1 = {"a": 1, "b": [10, 20]}
# d2 = d1.?                                                   # Создаем поверхностную копию
# print(d1 is d2)                                                  # Это разные объекты
# # False
# d2["a"] = 800                                                    # Изменяем значение
# print(d1, d2)                                                    # Изменилось значение только в d2
# # ({'a': 1, 'b': [10, 20]}, {'a': 800, 'b': [10, 20]})
# d2["b"][0] = "new"                                               # Изменяем значение вложенного списка
# print(d1, d2)                                                    # Изменились значения и в d1, и в d2!!!
# # ({'a': 1, 'b': ['new', 20]}, {'a': 800, 'b': ['new', 20]})
