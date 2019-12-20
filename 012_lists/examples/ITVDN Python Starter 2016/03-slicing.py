# -*- coding: utf-8 -*-

# Можно получить группу элементов по их индексам.
# Эта операция называется срезом списка (list slicing).

# Создание списка чисел
my_list = [5, 7, 9, 1, 1, 2]

# Получение среза списка от нулевого (первого) элемента (включая его)
# до третьего (четвёртого) (не включая)
sub_list = my_list[0:3]
# Вывод полученного списка
print(sub_list)

# Вывод элементов списка от второго до предпоследнего
print(my_list[2:-2])
# Вывод элементов списка от четвёртого (пятого) до пятого (шестого)
print(my_list[4:5])