# # -*- coding: utf-8 -*-
#
# s _    # set
# print ?
# # set([])
#
#
# print ___ "string                 # Преобразуем строку
# # set(['g', 'i', 'n', 's', 'r', 't'])
# print ___ 1, 2, 3, 4, 5            # Преобразуем список
# # set([1, 2, 3, 4, 5])
# print ___ 1, 2, 3, 4, 5          # Преобразуем кортеж
# # set([1, 2, 3, 4, 5])
# print ___ 1, 2, 3, 1, 2, 3  # Остаются только уникальные элементы
# # set([1, 2, 3])
#
#
# ___ i __ ___ 1, 2, 3
#   print ?
# # 1 2 3
#
#
# print le. ___ 1, 2, 3
# # 3
#
#
# s = ___ 1, 2, 3
# print ?.u.. ___ 4, 5, 6, ? @ ___ 4, 5, 6
# # (set([1, 2, 3, 4, 5, 6]), set([1, 2, 3, 4, 5, 6]))
#
#
# print ___ 1, 2, 3 @ ___ 1, 2, 3
# # set([1, 2, 3])
#
#
# s = ___ 1, 2, 3
# ?.up.. ___ 4, 5, 6
# print ?
# # set([1, 2, 3, 4, 5, 6])
# ? @_ ___ 7, 8, 9
# print ?
# # set([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
#
# print ___ 1, 2, 3 @ ___ 1, 2, 4
# # set([3])
# s = ___ 1, 2, 3
# print(?.d.. ___ 1, 2, 4]
# # set([3])
#
#
# s = ___ 1, 2, 3
# ?.d_u. ___ 1, 2, 4
# print ?
# # set([3])
# ? @_ ___ 3, 4, 5
# print ?
# # set([])
#
#
# print ___ 1, 2, 3 @ ___ 1, 2, 4
# # set([1, 2])
# s = ___ 1, 2, 3
# print ?.i.. ___ 1, 2, 4
# # set([1, 2])
#
#
# s = ___ 1, 2, 3
# ?.i_u.. ___ 1, 2, 4
# print ?
# # set([1, 2])
# ? @_ ___ 1, 6, 7
# print ?
# # set([1])
#
#
# s = ___([1, 2, 3])
# print ? @ ___ 1, 2, 4 , ?.s_d. ___ 1, 2, 4
# # (set([3, 4]), set([3, 4]))
# print ? @ ___ 1, 2, 3 , ?.s_d. ___ 1, 2, 3
# # (set([]), ___([]))
# print(? @ ___ 4, 5, 6, ?.s_d. ___ 4, 5, 6
# # (set([1, 2, 3, 4, 5, 6]), set([1, 2, 3, 4, 5, 6]))
#
#
# s = ___([1, 2, 3])
# ?.s_d_u. ___ 1, 2, 4
# print ?
# # set([3, 4])
# ? @_ ___ 3, 5, 6
# print ?
# # set([4, 5, 6])
#
#
# s = ___ 1, 2, 3, 4, 5
# print(1 __ ?, 12 __ ?
# # (True, False)
#
#
# s = ___ 1, 2, 3, 4, 5
# print(1 __ ?, 12 __ ?
# # (False, True)
#
#
# print ___ 1, 2, 3 __ ___ 1, 2, 3
# # True
# print ___ 1, 2, 3 __ ___ 3, 2, 1
# # True
# print ___ 1, 2, 3 __ ___ 1, 2, 3, 4
# # False
#
#
# s = ___ 1, 2, 3
# print ? @_ ___ 1, 2 , ? @_ ___([1, 2, 3, 4
# # (False, True)
# print ?.issu.. ___ 1, 2, ?.issu.. ___ 1, 2, 3, 4
# # (False, True)
#
#
# s = ___ 1, 2, 3
# print ? < ___ 1, 2, 3 , ? @ ___ 1, 2, 3, 4
# # (False, True)
#
#
# s = ___ 1, 2, 3
# print ? @_ ___ 1, 2  , ? @_ ___ 1, 2, 3, 4
# # (True, False)
# print ?.issu.. __ 1, 2  , ?.issu..(___ 1, 2, 3, 4
# # (True, False)
#
#
# s = ___ 1, 2, 3
# print ? @ ___ 1, 2  , ? @ ___ 1, 2, 3
# # (True, False)
#
#
# s = ___ 1, 2, 3
# print ?.isd.. ___ 4, 5, 6
# # True
# print ?.isd.. ___ 1, 3, 5
# # False
#
#
# s = ___ 1, 2, 3
# c = s; print(s __ c) # С помощью = копию создать нельзя!
# # True
# c = ?.c..  # Создаем копию объекта
# print(c)
# ___ 1, 2, 3
# print(s __ c       # Теперь это разные объекты
# # False
#
#
# s = ___ 1, 2, 3
# s.a.. 4; print ?
# # ___([1, 2, 3, 4])
#
# s = ___ 1, 2, 3
# s.re.. 3; print ?        # Элемент существует
# # set([1, 2])
# # s.remove(5)           # Элемент НЕ существует
# # Traceback (most recent call last):
# #   File "<pyshell#78>", line 1, in <module>
# #     s.remove(5)           # Элемент НЕ существует
# # KeyError: 5
#
#
# s = ___ 1, 2, 3
# s.di..  3; print ?       # Элемент существует
# # set([1, 2])
# s.di.. 5; print ?       # Элемент НЕ существует
# # set([1, 2])
#
#
# s = ___ 1, 2
# s.p.. , print ?
# # (1, set([2]))
# s.p.. , print ?
# # (2, set([]))
# # s.pop() # Если нет элементов, то будет ошибка
# # Traceback (most recent call last):
# #   File "<pyshell#89>", line 1, in <module>
# #     s.pop() # Если нет элементов, то будет ошибка
# # KeyError: 'pop from an empty set'
# #
#
# s = ___ 1, 2, 3
# s.cl.. ; print(s)
# # ___([])
#
#
# print x ___ ? __ 1, 2, 1, 2, 1, 2, 3
# # {1, 2, 3}
#
#
# print x ___ ? __ 1, 2, 1, 2, 1, 2, 3 i_ ? % 2 __ 0
# # {2}
#
#
# f = f..
# print ?
# # frozenset([])
#
#
# print f.. string                   # Преобразуем строку
# # frozenset(['g', 'i', 'n', 's', 'r', 't'])
# print f.. 1, 2, 3, 4, 4           # Преобразуем список
# # frozenset([1, 2, 3, 4])
# print f.. 1, 2, 3, 4, 4             # Преобразуем кортеж
# # frozenset([1, 2, 3, 4])