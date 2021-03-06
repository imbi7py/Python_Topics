# # -*- coding: utf-8 -*-
#
# # Сопрограммы в Python
#
# # Предлагаю обсудить такую интересную, но мало используемую возможность python, как сопрограммы (coroutines).
# # Сопрограммы в питоне основаны на генераторах (ими, они, собственно и являются).
# # Поэтому, предлагаю начать именно с генераторов, в общем понимании. А потом разберём как написать свою сопрограмму.
# #
# # Генераторы
# #
# # Любой более-менее приличный программист на Python знает, что есть такая замечательная штука, как функции-генераторы.
# # Главная их особенность — это сохранение состояния между вызовами.
# # Я подразумеваю что вы знаете как они работают, поэтому просто напомню, как это выглядит.
# # Возьмём вот такую функцию:
#
# ___ read_file_line_by_line file_name
#   w__ o.. ? _ __ f        # open for read
#       w___ T..
#         line _ ?.r.l.
#         __ no. ?
#           b___
#         y.... ?
#
# # Эта функция принимает на вход имя файла и возвращает его строчка за строчкой, не загружая целиком в память,
# # что может быть необходимо при чтении больших файлов.
# # Такой приём называют ленивым (lazy) чтением, подразумевая, что мы не делаем «работу» без необходимости.
# # В общем случае, работа с генераторами выглядит следующим образом:
#
# lines_generator = ? data.csv
# print ty.. ?
# # Out[79]: generator
#
# ?.ne..
# # Out[83]: 'time,host,event\n'
#
# ?.ne..
# # Out[84]: '1374039728,localhost,reboot\n'
#
# ?.ne..
# # Out[85]: '1374039730,localhost,start\n'
#
# ?.ne..
#
# # ---------------------------------------------------------------------------
# #
# # StopIteration                             Traceback (most recent call last)
# # <ipython-input-86-65df1a2cb71b> in <module>()
# # ----> 1 lines_generator.next()
# # StopIteration:
#
# # Соответственно у меня в файле только 3 строчки
# # Как только читать больше нечего, возникает исключение StopIteration, как и с любым итерируемым оъектом.
#
# # Естественно, чаще мы читаем значения из генератора в цикле, а не построчно.
# # Вот таким нехитрым способом мы можем получить все уникальные строки из сколь угодно большого файла:
#
# uniq _    # list
# ___ line __ ?
#   __ ? no. __ ?
#       ?.ap.. l..
#
#
# # Так же возможна короткая запись генератора:
#
# gen _  x ___ ? __ ra.. 0, 100*10000
# ?.ne..
# # Out[93]: 0
#
# ?.ne..
# # Out[94]: 1
#
# ?.ne..
# # Out[95]: 2
#
# ?.ne..
# # Out[96]: 3
#
# ?.ne..
# # Out[97]: 4
#
#
# # Похоже на списковые выражения, верно? Только не требует создания всего списка range(0, 100*10000) в памяти,
# # возвращаемое значение «вычисляется» каждый раз при обращении.
# # Сопрограммы как частный случай генераторов
# # А теперь о том, ради чего это, собственно, затевалось. Оказывается, генератор может не только возвращать значения,
# # но и принимать их на вход.
# # О стандарте можно почитать тут PEP 342.
# # Предлагаю сразу начать с примера. Напишем простую реализацию генератора, который может складывать два аргумента,
# # хранить историю результатов и выводить историю.
#
# ___ calc
#     history =       # list
#     w___ T..
#         x, y _ |y...
#         __ x __ 'h':
#             print ?
#             c______
#         result _ x + y
#         print r...
#         ?.ap.. r...
#
# c = calc
#
# print ty.. ? # <type 'generator'>
#
# c.ne.. # Необходимая инициация. Можно написать c.send(None)
# c.se..((1,2)) # Выведет 3
# c.se..((100, 30)) # Выведет 130
# c.se..((666, 0)) # Выведет 666
# c.se..(('h',0)) # Выведет [3, 130, 666]
# c.cl..  # Закрывем генератор
#
# # Т.е. мы создали генератор, проинициализировали его и подаём ему входные данные.
# # Он, в свою очередь, эти данные обрабатывает и сохраняет своё состояние между вызовами до тех пор пока
# # мы его не закрыли. После каждого вызова генератор возвращает управление туда, откуда его вызвали.
# # Это важнейшее свойство генераторов мы и будем использовать.
# # Так, с тем, как это работает, вроде, разобрались.
# # Давайте теперь избавим себя от необходимости каждый раз руками инициализировать генератор.
# # Решим это типичным, для питона, образом, с помощью декоратора.
#
# ___ coroutine f
#     ___ wrap $ $$
#         gen _ _ $ $$
#         ?.se.. N..
#         r___ ?
#
#     r_ ?
#
#
# ??
# ___ calc
#     history _     # list
#     w___ T..
#         x, y = |y..
#         __ x __ 'h':
#             print ?
#             c...
#         result = x + y
#         print ?
#         ?.ap. r..
#
# # На этом примере можно понять как писать свои более сложные (и полезные) сопрограммы.
# # Заключение.
# # Хоть проблемы, которые можно решить этим инструментом затрагивают очень многие области
# # (такие как асинхронное программирование), многие разработчики предпочитают более привычные инструменты ООП.
# # Но при этом сопрограммы могут быть очень полезным инструментом в вашем арсенале, поскольку они достаточно наглядны,
# # а создание фунций более дешёвая операция по сравнению с созданием объекта класса.
# # Да и определённый академический интерес они представляют, как мне кажется.
