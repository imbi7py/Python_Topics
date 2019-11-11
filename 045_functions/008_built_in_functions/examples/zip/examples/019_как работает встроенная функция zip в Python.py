# Многие слышали о функции zip в Python, а кто-то даже регулярно ей пользуется.
# Сегодня мы (из интереса и для общего развития) опишем, как можно реализовать её самому с помощью list comprehensions.
#
# Для начала поясню, что вообще делает функция zip, для тех, кто с ней раньше не сталкивался:

s = 'abc'
t = (10, 20, 30)
zip(s,t)
# [('a', 10), ('b', 20), ('c', 30)]

# То есть функция берёт на вход несколько списков и создаёт из них список (в Python 3 создаётся не list,
# а специальный zip-объект) кортежей, такой, что первый элемент полученного списка содержит кортеж из первых элементов
# всех списков-аргументов. Таким образом, если ей передать три списка, то она отработает следующим образом:

s = 'abc'
t = (10, 20, 30)
u = (-5, -10, -15)

list(zip(s,t,u))
# [('a', 10, -5), ('b', 20, -10), ('c', 30, -15)]

# В общем-то, функция отработает даже для одного iterable-объекта, результатом будет последовательность из кортежей,
# в каждом из которых будет по одному элементу. Но это, пожалуй, не самый распространенный способ применения zip.
# Я часто использую zip, например, для создания словарей:

names = ['Tom', 'Dick', 'Harry']
ages = [50, 35, 60]

dict(zip(names, ages))

# {'Harry': 60, 'Dick': 35, 'Tom': 50}

# Это весьма удобно, не находите? Каждый раз, когда я рассказываю о zip на своих уроках, у меня спрашивают о том,
# что будет, если в функцию передать массивы разной длины. Ответ простой — победит более короткий:

s = 'abc'
t = (10, 20, 30, 40)
list(zip(s,t))
# [('a', 10), ('b', 20), ('c', 30)]

# Однако, если вам необходимо, чтобы для каждого из элементов более длинного массива в результирующем списке
# был создан кортеж из одного элемента, вы можете использовать zip_longest из пакета itertools.
#
# Есть одна возможность в Python, которая мне нравится даже больше, чем zip. Это списковое включение
# (англ. list comprehension). Именно поэтому, когда один из студентов недавно спросил меня, можем ли мы реализовать
# zip сами с помощью списковых включений, я просто не смог устоять.
#
# Как же нам этого добиться? Начнём с первого, что приходит на ум:

[(s[i], t[i])              # создаём кортеж из двух элементов
 for i in range(len(s))]   # для индексов от 0 до len(s) - 1


s = 'abcd'
t = (10, 20, 30)
sorted((s,t), key=len)
# [(10, 20, 30), 'abcd']

# Совмещаем это с предыдущим кодом:

s = 'abcd'
t = (10, 20, 30)

sorted((s,t), key=len)
# [(10, 20, 30), 'abcd']

# Это ещё не все доработки, а выражение уже получается слишком длинным.
# Пожалуй, выяснение наименьшей длины стоит вынести в отдельную функцию (заодно сделаем так,
# чтобы она вычисляла наикратчайшую последовательность из неограниченного количества аргументов):

def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))

[(s[i], t[i])for i in shortest_sequence_range(s,t) ]

# Что осталось теперь? Как уже говорилось выше, Python 3 создаёт не список, а специальный zip-объект,
# возвращая итератор от него. Это сделано для того, чтобы код не ломался при обработке исключительно длинных
# последовательностей. Это можно реализовать, но уже не с помощью спискового включения
# (которое всегда возвращает список), а с помощью генератора. К счастью, для этого достаточно поменять квадратные
# скобки на круглые:

def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))

g = ((s[i], t[i]) for i in shortest_sequence_range(s,t) )

for item in g:
    print(item)

# ('a', 10)
# ('b', 20)
# ('c', 30)

# Готово! Мы реализовали свой полностью рабочий zip. Вы можете потренироваться и самостоятельно подумать,
# как ещё можно улучшить этот алгоритм.