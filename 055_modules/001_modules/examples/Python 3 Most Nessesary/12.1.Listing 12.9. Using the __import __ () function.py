# -*- coding: utf-8 -*-
s = "test" + "s"            # Динамическое создание названия модуля
m = __import__(s)           # Подключение модуля tests
print(m.x)                  # Вывод значения атрибута x
input()