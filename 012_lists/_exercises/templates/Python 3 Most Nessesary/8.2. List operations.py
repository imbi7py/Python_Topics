# # -*- coding: utf-8 -*-
#
# arr = [1, "str", 3.2, "4"]
# print(? 0 ? 1 ? 2 ? 3
# # (1, 'str', 3.2, '4')
#
#
# x, y, z = [1, 2, 3] # Позиционное присваивание
# print(x, y, z)
# # (1, 2, 3)
# # x, y = [1, 2, 3]    # Количество элементов должно совпадать
# # Traceback (most recent call last):
# #   File "<pyshell#86>", line 1, in <module>
# #     x, y = [1, 2, 3]    # Количество элементов должно совпадать
# # ValueError: too many values to unpack (expected 2)
#
#
# x, y, *z = [1, 2, 3];  print(x, y, z)
# # (1, 2, [3])
# x, y, *z = [1, 2, 3, 4, 5]; print(x, y, z)
# # (1, 2, [3, 4, 5])
# x, y, *z = [1, 2]; print(x, y, z)
# # (1, 2, [])
# *x, y, z = [1, 2]; print(x, y, z)
# # ([], 1, 2)
# x, *y, z = [1, 2, 3, 4, 5]; print(x, y, z)
# # (1, [2, 3, 4], 5)
# *z, = [1, 2, 3, 4, 5]; print(z)
# # [1, 2, 3, 4, 5]
#
#
# arr = [1, 2, 3, 4, 5]
# print(le. ?            # Получаем количество элементов
# # 5
# print ? le. ? -_       # Получаем последний элемент
# # 5
#
#
# arr = [1, 2, 3, 4, 5]
# # print(arr[5])                # Обращение к несуществующему элементу
# # Traceback (most recent call last):
# #   File "<pyshell#99>", line 1, in <module>
# #     arr[5]                # Обращение к несуществующему элементу
# # IndexError: list index out of range
#
#
# arr = [1, 2, 3, 4, 5]
# print(? -_, ? l.. ?-_  # Обращение к последнему элементу
# # (5, 5)
#
#
# arr = [1, 2, 3, 4, 5]
# arr[0] = 600             # Изменение элемента по индексу
# print(arr)
# # [600, 2,print( 3, 4, 5]
#
#
# arr = [1, 2, 3, 4, 5]
# m = ? _ ;  print(m)  # Создаем поверхностную копию и выводим значения
# # [1, 2, 3, 4, 5]
# print(m i_ arr)      # Оператор is показывает, что это разные объекты
# # False
#
#
# arr = [1, 2, 3, 4, 5]
# print(? _ _ -1             # Шаг -1
# # [5, 4, 3, 2, 1]
#
#
# print ? _               # Без первого элемента
# # [2, 3, 4, 5]
# print ? -_              # Без последнего элемента
# # [1, 2, 3, 4]
#
#
# print ? 0 _              # Символ с индексом 2 не входит в диапазон
# # [1, 2]
#
#
# print ? -_              # Последний элемент списка
# # [5]
#
#
# print ? _ _ # Возвращаются элементы с индексами 1, 2 и 3
# # [2, 3, 4]
#
#
# arr = [1, 2, 3, 4, 5]
# ? _  _ _ [6, 7] # Изменяем значения элементов с индексами 1 и 2
# print ?
# # [1, 6, 7, 4, 5]
# ? _ _ _ _ []     # Удаляем элементы с индексами 1 и 2
# print ?
# # [1, 4, 5]
#
#
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [6, 7, 8, 9]
# arr3 = arr1 + arr2
# print(arr3)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# arr = [1, 2, 3, 4, 5]
# arr += [6, 7, 8, 9]
# print(arr)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# print([1, 2, 3] * 3)                              # Операция повторения
# # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(2 in [1, 2, 3, 4, 5], 6 in [1, 2, 3, 4, 5]) # Проверка на вхождение
# # (True, False)