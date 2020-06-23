# -*- coding: utf-8 -*-

# up...
# uрdаtе <Список кортежей с двумя элементами>

d = {"a": 1, "c": 3, "b": 2, "d": 4}
d.update([("d", 80), ("e", 6)])
# Список кортежей
print(d)

# update
# uрdаtе <Список списков с двумя элементами>
d = {"a": 1, "c": 3, "b": 2, "d": 4}
d.update([["a", "str"], ["i", "t"]])    # Список списков
print(d)

# # сору
# # создает поверхностную копию словаря:
# d1 _ "a" 1 "b" |10, 20|
# d2 _ d1.co..    # Создаем поверхностную копию
# print d1 i. d2     # Это разные объекты
# # False
# d2|"a"| _ 800   # Изменяем значение
# print d1 d2   # Изменилось значение только в d2
# #  'a': 1, 'b': |10, 20|, 'a': 800, 'b': |10, 20|
# d2|"b"||0| _ "new"   # Изменяем значение вложенного списка
# print d1 d2    # Изменились значения и в d1, и в d2!!!
# #  'a': 1, 'b': |'new', 20|, 'a': 800, 'b': |'new', 20|

# Генераторы словарей
keys = ["a", "b"]  # Список с ключами
values = [1, 2] # Список со значениями
print({k: v for k, v  in zip(keys, values)})
#  'a': 1, 'b': 2
print({k: 0 for k in keys})
#  'a': 0, 'b': 0
d = {"a": 1, "b": 2, "c": 3, "d": 4}
print({k: v for (k, v) in d.items() if v % 2 == 0})
# # 'b': 2, 'd': 4

# di.. keyword argument form
print(dict(name='mel', age=45))

# di.. key/value tuples form
print(dict([('name', 'mel'), ('age', 45)]))

# z.. together keys and values
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# Make a di.. from z.. result
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))

# di.. comprehension
D = {k: v for k, v in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

# di.. comprehension
# Or: range 1, 5
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

# di.. comprehension
# Loop over any iterable
D = {c: c * 4 for c in 'SPAM'}
print(D)

D = {c.lower(): c + '!' for c in ['SPAM' 'EGGS' 'HAM']}
print(D)

# Initialize di.. from keys
# with a comprehension
D = dict.fromkeys(['a', 'b', 'c'], 0)
# Initialize di.. from keys
print(D)
D = {k: 0 for k in ['a', 'b', 'c']}
# Same, but with a comprehension
print(D)

# len d  – количество элементов.
phonebook ={
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

print(len(phonebook('entries found')))

# d|key|
# получение значения с ключом key. Если такой ключ не существует
# # и отображение реализует специальный метод __missing__ self, key , то он
# # вызывается. Если ключ не существует и метод __missing__ не определён,
# # выбрасывается исключение KeyError.
#
try:
    print('Mary:', phonebook['Mary'])
    print('Lumberjack:', phonebook|'Lumberjack'|
except KeyError as e:
    print('No entry for', *e.args)

# d|key| _ value
# value – изменить значение или создать новую пару ключ-значение, если ключ не существует.
#
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

phonebook['Lumberjack'] = '000-777'

# key in d, key not in d – проверка наличия ключа в отображении.
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

for person in ('Guido', 'Mary', 'Ahmed'):
    if person in phonebook:
        print(person, 'is in the phonebook')
    else:
        print('No entry found for', person)

print()

# iter d  – то же самое, что iter d.keys )).
phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

print 'People in the phonebook:'
___ person __ ?
    print ?

print

# co..   – создать неполную копию словаря.
phonebook _
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется


phonebook_copy _ ?.co..
print 'Phonebook:', ph...
print 'Phonebook co..:', ph.._cop..

# clear   – удалить все элементы словаря.
phonebook _
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется


phonebook_copy.clear
print 'Phonebook:', ph...
print 'Phonebook co..:', ph.._c..

di...f... sequence| value|  – # создаёт новый словарь с
# ключами из последовательности sequence и заданным значением  по умолчанию –
None .