# # -*- coding: utf-8 -*-
#
# ______ c____            # Подключаем модуль copy
# x = [1, [2, 3, 4, 5]]
# y = c___.d___ x    # Делаем полную копию списка
# y 1 1 _ 100           # Изменяем второй элемент
# print(x, y)                  # Изменился только список в переменной y
# # ([1, [2, 3, 4, 5]], [1, [2, 100, 4, 5]])
#
#
# _______ c___          # Подключаем модуль copy
# x = [1, 2]
# y = [x, x]           # Два элемента ссылаются на один объект
# print(y)
# # [[1, 2], [1, 2]]
# z = c___.d___ y # Сделали копию списка
# print(z 0 i_ x, z[1] i_ x, z 0 i_ z 1
# # (False, False, True)
# z 0 0 = 300        # Изменили один элемент
# print(z)                    # Значение изменилось сразу в двух элементах!
# # [[300, 2], [300, 2]]
# print(x)                    # Начальный список не изменился
# # [1, 2]