# -*- coding: utf-8 -*-

# generator-expressions

# Некоторые простые генераторы могут быть записаны в виде выражения.
# Они выглядят как выражение, содержащее некоторые переменные, после
# которого одно или несколько ключевых слов for, задающих, какие значения
# должны принимать данные переменные (синтаксис соответствует заголовку
#     цикла for), и ноль или несколько условий, фильтрующих генерируемые
# значения (синтаксис соответствует заголовку оператора if). Такие выражения
# называются выражениями-генераторами (generator expressions).
#
generator = (x ** 2 + y for x in range(2, 7) for y in range(3) if x != 6)
for number in generator:
    print(number)

print()

print(sum(2 * x for x in range(5)))

# delegating-to-subgenerator

# В Python 3 существуют так называемые подгенераторы (subgenerators).
# Если в функции-генераторе встречается пара ключевых слов yield from,
# после которых следует объект-генератор, то данный генератор делегирует
# доступ к подгенератору, пока он не завершится (не закончатся его значения),
# после чего продолжает своё исполнение.
#
#
def generator():
    yield from (3 * x for x in range(5))
    yield from (2 * x for x in range(5, 10))


for i in generator():
    print(i)
