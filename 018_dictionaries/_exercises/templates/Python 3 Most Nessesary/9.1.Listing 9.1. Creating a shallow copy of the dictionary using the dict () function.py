# -*- coding: utf-8 -*-

d1 = {"a": 1, "b": 2}        # Создаем словарь
d2 = dict(d1)                  # Создаем поверхностную копию
print(d1 is d2)                # Оператор показывает, что это разные объекты
# False
d2["b"] = 10
print(d1, d2)                  # Изменилось только значение в переменной d2
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 10})
