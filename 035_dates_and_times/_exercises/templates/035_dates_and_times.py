# -*- coding: utf-8 -*-

# time ( )
# возвращает вещественное число, представляющее количество секунд, прошедшее
# с начала эпохи (обычно с 1 января 1970 г.):

# ______ ?
# ?.ti..

"""
# gmtime ( [<Количество секунд>])
"""
#
# возвращает объект struct_time, представляющий
# универсальное время (UTC). Если параметр не указан, то возвращается текущее время.
# Если параметр указан, то время будет не текущим, а соответствующим количеству
# секунд, прошедших с начала эпохи.
#
# Получить значение конкретного атрибута можно, указав его название или индекс внутри
# объекта:
#
# # Преобразование в кортеж

# ?.g.. 0 # Начало эпохи
# ?.g..  # Текущая дата и время
# ?.g.. 1428057929.0 # Дата 03-04-2015
# 
# d = ?.?
# ?.tm_year, ? 0
# # (2015, 2015)
# 
# tu.. d

"""
# localtime ( [<Количество секунд>])
"""
#
# возвращает объект struct_time, представляющий
# локальное время. Если параметр не указан, то возвращается текущее время. Если параметр
# указан, то время будет не текущим, а соответствующим количеству секунд, прошедших
# с начала эпохи.

# ?.l...  # # Текущая дата и время
# ?.l... 1428057929.0
# # Дата 03-04-2015

"""
# mktirne (<Объект struct_tirne>)
"""
#
# возвращает вещественное число, представляющее количество
# секунд, прошедших с начала эпохи. В качестве параметра указывается объект
# struct_tirne или кортеж из девяти элементов. Если указанная дата некорректна, возбуждается
# исключение OverflowError.

# d = ?.l... 1428057929.0
# ?.m.. ?
# # 1428057929.0
# tu.. ?.l...1428057929.0
# # (2015, 4, 3, 13, 45, 29, 4, 93, 0)
# ?.m.. 2015, 4, 3, 13, 45, 29, 4, 93, 0
# # 1428057929.0
# ?.m.. 1940, 0, 31, 5, 23, 43, 5, 31, 0

# ... Фрагмент опущен ...
# OverflowError: mktime argument out of range

# Объект struct_time, возвращаемый функциями gmtime () и localtime (), содержит следующие
# атрибуты (указаны пары вида «имя атрибута - индекс - описание»):

# trn_year - О - год;
# tm_mon- 1 - месяц (число от 1 до 12);
# tm rnday - 2 - день месяца (число от 1 до 31);
# tm_hour - з - час (число от о до 23);
# tm_mir. - 4 - минуты (число от о до 59):
# tm_sec - 5 - секунды (число от о до 59, изредка до 61);
# tm_wday - б - день недели (число от о для понедельника до 6 для воскресенья);
# tm_yday- 7 - количество дней, прошедшее с начала года (число от 1 до 366);
# tm_isdst. - 8 - флаг коррекции летнего времени (значения о, 1 или -1).

# Display current date and ?
# ______ ti..  # Подключаем модуль time
# d = ["понедельник", "вторник", "среда", "четверг",
#       "пятница", "суббота", "воскресенье" ]
# m = ["", "января", "февраля", "марта", "апреля", "мая",
#       "июня", "июля", "августа", "сентября", "октября",
#       "ноября", "декабря" ]
# t = ?.l...  # Получаем текущее время
# print("Сегодня:\n%s %s %s %s %02d:%02d:%02d\n%02d.%02d.%02d" %
#       (d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t[5], t[2], t[1], t[0]))
# input()

# Форматирование даты
# ______ ?
# ?.str.. @.@.@     # day|month|year
# 
# ?.str.. @ @ @ ?.l... 1321954972.0  # day|month|year
# 
# # Форматирование времени
# ?.str.. @ @ @                    # hour|minute|sec

"""
# strptime(<Cтpoкa с датой>[, <Строка формата>])
"""
#
# разбирает строку, указанную в
# первом параметре, в соответствии со строкой формата. Возвращает объект struct_time.
# Если строка не соответствует формату, возбуждается исключение ValueError. Если
# строка формата не указана, используется строка "%а %Ь %d %Н: %М: %S %У".
# ?.s.. Fri Apr 03 14:01:34 2015
# ?.s.. 03.04.2015 @ @ @    # day|month|year
# ?.s.. 03-04-2015 @ @ @    # day|month|year

"""
# asctirne( [<Объект struct_time>])
"""
#
# возвращает строку формата "%а %Ь %d %H:%M:%S
# %У". Если параметр не указан, будут выведены текущие дата и время. Если в параметре
# указан объект struct_time или кортеж из девяти элементов, то дата будет соответствовать
# указанному значенmо.
# ?.a..                             # Текущая дата
# # 'Fri Apr  3 14:06:12 2015'
# ?.a.. ?.l... 1321954972.0  # Дата в прошлом
# # 'Tue Nov 22 12:42:52 2011'

"""
# ctime < [ <Количество секунд> J ) -
"""
#  функция аналогична asctirne (), но в качестве параметра
# принимает не объект struct_tirne, а количество секунд, прошедших с начала эпохи.
# ?.c..                    # Текущая дата
# # 'Fri Apr  3 14:06:12 2015'
# ?.c.. 1321954972.0        # Дата в прошлом
# # 'Tue Nov 22 12:42:52 2011'

# В параметре <Строка формата> в функциях strftirne () и strptime () моrут быть использованы
# следующие комбинации специальных символов:
# %у- год из двух цифр (от "ОО" до "99");
# %У- год из четырех цифр (например, "2011 ");
# %rn- номер месяца с предваряющим нулем (от "01" до "12");
# %Ь - аббревиаlУJ)а месяца в зависимости от настроек локали {например, " янв" для января);
# %В- название месяца в зависимости от настроек локали (например, "Январь");
# %d- номер дня в месяце с предваряющим нулем (от "01" до "31 ");
# %j - день с начала года (от "001" до "366");
# %U - номер недели в году (от "00" до "53"). Неделя начинается с воскресенья. Все дни
# начала года до первого воскресенья относятся к неделе с номером о;
# %W- номер недели в году (от "ОО" до "53"). Неделя начинается с понедельника. Все дни
# начала года до первого понедельника относятся к неделе с номером о;
# %w - номер дня недели ("О" - для воскресенья, "б" - для субботы);
# %а - аббревиатура дня недели в зависимости от настроек локали (например, "Пн" для
# недельника);
# %А - название дня недели в зависимости от настроек
#
# %! - часы в 12-часовом формате (от "01" до "12");
# %М- минуты (от "ОО" до "59");
# %S - секунды (от "ОО" до "59", изредка до "61 ");
# %р - эквивалент значениям АМ и РМ в

# В параметре <Строка формата> в функциях strftirne () и strptime () моrут быть использованы
# следующие комбинации специальных символов:
# ______ lo__
# lo__.s_l_ lo__.L_A. Russian_Russia.1251
# # 'Russian_Russia.1251'
# print(?.s.. @   # Представление даты
# # 03.04.2015
# print(?.s.. @   # Представление времени
# # 14:10:19
# print(?.s.. @   # Дата и время
# # 03.04.2015 14:10:19
# 
# # Date and time formatting
# ______ ?
# ______ lo__
# lo__.setl lo__.L_A Russian_Russia.1251
# s = "Сегодня:\n%A @ @ % @ @ @\n@ @ @"   # day|аббревиаlУJ)а месяца|year|hour|minute|sec  day|month|year
# print ?.str.. ?
# input()

# Модуль ctatetime
# Модуль ctatetime позволяет манипулировать датой и временем. Например, выполнять
# арифметические операции, сравнивать даты, vыводить дату и время в различных форматах
# и др. Прежде чем использовать классы из этого модуля, необходимо подключить модуль
# с ПОМОЩЬЮ инструкции
#
# Модуль содержит пять классов:
# + timedelta - дата в виде количества дней, секунд и микросекунд. Экземпляр этого класса
# можно складывать с экземплярами классов date и datetime. Кроме того, результат
# вычитания двух дат будет экземпляром класса timedelta;
# + date - представление даты в виде объекта;
# + time - представление времени в виде объекта;
# + datetime - представление комбинации даты и времени в виде объекта;
# + tzinfo- абстрактный класс, отвечающий за зону времени. За подробной информацией
# по этому классу обращайтесь к документации по модулю datetime.

"""
# timedelta
"""
# Класс timedelta из модуля datetime позволяет выполнять операции над датами - например:
# складывать, вычитать, сравнивать и др. Конструктор класса имеет следующий формат:
# timedelta([days] [, seconds] [, microseconds] [, milliseconds] [, minutes]
# [ , hours] [, wee ks] )
# Все параметры не являются обязательными и по умолчанmо имеют значение о. Первые три
# параметра считаются основными:
# 
# # timedelta
# # milliseconds
# ______ d_t_
# d_t_.? mi.._1
# 
# # timedelta
# # minutes
# 
# d_t_.? m.._1
# 
# # timedelta
# # hours
# d_t_.? h.._1
# 
# # timedelta
# # weeks
# d_t_.? w.. 1

# # Значения можно указывать через запятую в порядке следования параметров или присвоить
# # значение названию параметра. В качестве примера укажем опин час:
# d_t_.t_d_ 0, 0, 0, 0, 0, 1
# # datetime.timedelta(0, 3600)
# d_t_.t_d_ h.. 1
# # datetime.timedelta(0, 3600)
# 
# # Получить результат можно с помощью следующих атрибутов:
# # + dауs-дни;
# # + seconds - секунды;
# # + microseconds - микросекунды.
# d = d_t_.t_d_ h.. 1 d.. 2 mi.. 1
# d
# # datetime.timedelta(2, 3600, 1000)
# ?.d.. ?.s... ?.mi..
# # (2, 3600, 1000)
# re.. ? st. ?
# # ('datetime.timedelta(2, 3600, 1000)', '2 days, 1:00:00.001000')
# 
# # Получить результат в секундах позволяет метод total _ seconds () :
# d = d_t_.t_d_ m.. 1
# ?.t_s..
# # 60.0

# Над экземrшярами класса tirnedelta можно производить арифметические операции +, -, /,
# / /, % и *, использовать унарные операторы + и - , а также получать абсолютное значение
# с помощью функции abs ()
# d1 = d_t_.t_d_(d 2)
# d2 = d_t_.t_d_(d 7)
# d1 + d2, d2 — d1                          # Сложение и вычитание
# # (datetime.timedelta(9), datetime.timedelta(5))
# d2 / d1                                   # Деление
# # 3.5
# d1 / 2, d2 / 2.5                          # Деление
# # (datetime.timedelta(1), datetime.timedelta(2, 69120))
# d2 // d1                                  # Деление
# # 3
# d1 // 2, d2 // 2                          # Деление
# # (datetime.timedelta(1), datetime.timedelta(3, 43200))
# d2 % d1                                   # Остаток
# # datetime.timedelta(1)
# d1 * 2, d2 * 2                            # Умножение
# # (datetime.timedelta(4), datetime.timedelta(14))
# 2 * d1, 2 * d2                            # Умножение
# # (datetime.timedelta(4), datetime.timedelta(14))
# d3 = -d1
# d3, abs(d3)
# # (datetime.timedelta(-2), datetime.timedelta(2))

# Кроме того, можно использовать операторы сравнения =, ! =, <, <=, > и >=.
# d1 = d_t_.t_d_(d 2)
# d2 = d_t_.t_d_(d 7)
# d3 = d_t_.t_d_(w.. 1)
# d1 == d2, d2 == d3                # Проверка на равенство
# # (False, True)
# d1 != d2, d2 != d3                # Проверка на неравенство
# # (True, False)
# d1 < d2, d2 <= d3                 # Меньше, меньше или равно
# # (True, True)
# d1 > d2, d2 >= d3                 # Больше, больше или равно
# # (False, True)
# 
# # Также можно получать строковое представление объекта timedelta с помощью функций
# # str () И repr ( ) :
# d = d_t_.t_d_ h..   25 m..   5 s..   27
# st. ?
# # '1 day, 1:05:27'
# re.. ?
# # 'datetime.timedelta(1, 3927)'

# Поддерживаются: следующие атрибуты класса:
# 5, seconds = 27)
# t min - минимальное значение, которое может иметь объект t imedel ta;
# • max- максимальное значение, которое может иметь объект tirnedelta;
# t resolution - минимальное возможное различие между значениями timedel ta.
# Выведем значения: этих атрибутов:
# d_t_.t_d_.mi.
# # datetime.timedelta(-999999999)
# d_t_.t_d_.ma.
# # datetime.timedelta(999999999, 86399, 999999)
# d_t_.t_d_.res..
# 
# # Класс date из модуля: datetirr.e позволяет выполнять операшm над датами. Конструктор
# # класса имеет следуюший формат:
# # dаtе(<Год>, <Месяu>, <День>:
# #
# # Все параметры являются обязательными. В параметрах можно указать следующий диапазон значений:
# 
# # Класс date из модуля: datetirr.e позволяет выполнять операшm над датами. Конструктор
# # класса имеет следуюший формат:
# # dаtе(<Год>, <Месяu>, <День>:
# #
# # Все параметры являются обязательными. В параметрах можно указать следующий диапазон значений:
# 
# # <Год> - в виде числа, расположенного в диапазоне между значениями, хранящимися
# # в константах MINYEAR и МАХУЕАR класса datetime (о нем речь пойдет позже). Выведем
# # значения этих констант:
# ______ d_t_
# d_t_.MI.. d_t_.MA..
# # (1, 9999)
# 
# # <Месяц> - от 1 до 12 вкmочительно;
# # + <День> - от 1 до количества дней в месяце.
# # Если значения выходят за диапазон, возбуждается искточение ValueError. Пример:
# d_t_.d.. 2015, 4, 3
# # datetime.date(2015, 4, 3)
# d_t_.d.. 2015, 13, 3   # Неправильное значение для месяца
# # ... Фрагмент опущен ...
# ValueError: month must be in 1..12
# d = d_t_.d.. 2015, 4, 3
# re.. ? st. ?
# # ('datetime.date(2015, 4, 3)', '2015-04-03')
# 
# # Для создания объекта класса date также можно воспользоваться следующими методами
# # этого класса:
# # today () - возвращает текущую дату:
# d_t_.d...t.. # Получаем текущую дату
# # datetime.date(2015, 4, 3)
# 
# d_t_.d...t.. # Получаем текущую дату
# # datetime.date(2015, 4, 3)
# 
# ______ d_t_, ?
# d_t_.d...fr.. ?.ti..  # Текущая дата
# # datetime.date(2015, 4, 3)
# d_t_.d...fr.. 1321954972.0 # Дата 22-11-2011
# # datetime.date(2011, 11, 22)

"""
# frornordinal (<Количество дней с 1-го года>)
"""
# - возвращает дату, соответствующую
# количеству дней, прошедших с первого года. В качестве параметра указывается число
# от 1 до datetirne. date .max. toordinal ().
# d_t_.d...ma_.too..
# # 3652059
# d_t_.d...f.. 3652059
# # datetime.date(9999, 12, 31)
# d_t_.d...f.. 1
# # datetime.date(1, 1, 1)

# Получить результат можно с помощью следующих атрибутов:
# + year - год (число в диапазоне от MINYEAR до МАХУЕАR);
# + month- месяц (число от 1 до 12);
# + day- день (число от 1 до количества дней в месяце).
# d = d_t_.d...t.. # Текущая дата (3-04-2015)
# ?.y.. ?.m.. ?.d..
# # (2015, 4, 3)

# Над экземплярами класса date можно производить следующие операции:
# 185
# t date2 = datel + tirnedelta - прибавляет к дате указанный период в днях. Значения
# атрибутов t irnedel ta. seconds и tirnedel ta. microseconds игнорируются;
# t date2 = datel - tirnedel ta - вычитает из даты указанный период в днях. Значения
# атрибутов timedelta.seconds и timedelta.microseconds игнорируются;
# t tirnedelta = datel - date2 - возвращает разницу между датами (период в днях). Атрибуты
# t irnede 1 ta. seconds и t imede 1 ta. microseconds будут иметь значение о;
# t можно также сравнивать две даты с помощью операторов сравнения.
# d1 = d_t_.d.. 2015, 4, 3
# d2 = d_t_.d.. 2015, 1, 1
# t = d_t_.t_d_(d 10)
# d1 + t, d1 — t             # Прибавляем и вычитаем 10 дней
# # (datetime.date(2015, 4, 13), datetime.date(2015, 3, 24))
# d1 — d2                    # Разница между датами
# # datetime.timedelta(92)
# d1 < d2, d1 > d2, d1 <= d2, d1 >= d2
# # (False, True, False, True)
# d1 == d2, d1 != d2
# # (False, True)

"""
replace ( [year] [, month] [, day]) -
"""
#  возвращает дату с обновленными значениями. Значения
# можно указывать через запятую в порядке следования параметров или присвоить
# значение названию параметра. Примеры:
# d = d_t_.d.. 2015, 4, 3
# ?.r.. 2014, 12 # Заменяем год и месяц
# # datetime.date(2014, 12, 3)
# ?.r..(y.. 2015 m.. 1 d.. 31
# # d_t_.date(2015, 1, 31)
# ?.r.. d.. 30   # Заменяем только день
# # datetime.date(2015, 1, 30)

"""
strftime (<Строка формата>!
"""

#  - возвращает отформатированную строку. В строке формата
# можно задавать комбинации специальных символов, которые используются
# в фуНКШfИ strftime, : из модуля time. Пример:
# d = d_t_.d.. 2015, 4, 3
# ?.s.. @ @ @
# '03.04.2015'

"""
isoformat ()
"""
#  -возвращает дату в формате гггг-мм-дд:
# d = d_t_.d.. 2015, 4, 3
# ?.i..
# '2015-04-03'

"""
ctime()
"""
#  -возвращает строку формата "%а %Ь %d %H:%M:%S %У":
# d = d_t_.d.. 2015, 4, 3
# ?.c..
# 'Fri Apr  3 00:00:00 2015'

"""
timetuple ()
"""
#  -возвращает объект struct_time с датой и временем:
# d = d_t_.d.. 2015, 4, 3
# ?.t..

"""
toordinal ()
"""
#  -возвращает количество дней, прошедших с 1-ro года:
# d = d_t_.d.. 2015, 4, 3
# ?.too..
# 735691
# d_t_.d...fromo.. 735691
# datetime.date(2015, 4, 3)

"""
weekday ( ) 
"""
# - возвращает порядковый номер дня в неделе ( о -для понедельника, 6 -
# для воскресенья):
# d = d_t_.d.. 2015, 4, 3
# ?.w. # 4 — это пятница
# 4

# d = d_t_.d.. 2015, 4, 3
# d.i_w_d_ # 5 — это пятница
# 5

"""
isoweekday ()
"""
#  - возвращает порядковый номер дня в неделе (1 - для понедельника,
# 7 -для воскресенья):
# d = d_t_.d.. 2015, 4, 3
# d.i.. # 5 — это пятница
# 5

"""
isocalendar ()
"""
#  -возвращает кортеж из трех элементов (год, номер недели в году и порядковый
# номер дня в неделе):
# d = d_t_.d.. 2015, 4, 3
# d.i..
# (2015, 14, 5)

# Наконец, имеется поддержка следующих атрибутов класса:
# • min -минимально возможное значение даты;
# • max -максимально возможное значение даты;
# • resolution - минимальное возможное различие между значениями даты.
# d_t_.d...mi.
# datetime.d..(1, 1, 1)
# d_t_.d...ma.
# datetime.date(9999, 12, 31)
# d_t_.d...res..
# datetime.timedelta(1)

# Класс time из модуля datetime позволяет выполнять операции над временем. Конструктор
# класса имеет следующий формат:
# time ( (hour] [, minute] [, second] [, microsecond] [, tzinfo])
# Все параметры не являются обязательными. Значения можно указывать через заru1тую
# в порядке следования параметров или присвоить значение названию параметра. В параметрах
# можно указать следующий диапазон значений:
# + hour - часы (число от о до 23);
# + minute - минуты (число от о до 59);
# + second- секунды (число от о до 59);
# + microsecond - микросекунды (число от О до 999999);
# + tzinfo - зона (экземпляр класса tzinfo или значение None).

# time из модуля datetime позволяет выполнять операции над временем. Конструктор
# класса имеет следующий формат:
# time ( (hour] [, minute] [, second] [, microsecond] [, tzinfo])
# ______ d_t_
# d_t_.? 23, 12, 38, 375000
# datetime.time(23, 12, 38, 375000)
# t = d_t_.? h.. 23 s.. 38 m.. 12
# re.. ? st. ?
# ('datetime.time(23, 12, 38)', '23:12:38')
# d_t_.? 25, 12, 38, 375000
# ... Фрагмент опущен ...
# ValueError: hour must be in 0..23

# Получить результат можно с помощью следующих атрибутов:
# + hour - часы (число от о до 23);
# + minute - минуть (число от о до 59);
# + second - секунды (число от о до 59);
# + · microsecond - микросекунды (число от о до 999999);
# + tzinfo - зона (экземпляр класса tzinfo или значение None).
# t = d_t_.? 23, 12, 38, 375000
# ?.h.. ?.m.. ?.s.. ?.mi..
# (23, 12, 38, 375000)

# Над экземплярами класса t ime нельзя выполнять арифметические операции. Можно только
# производить сравнения.
# t1 = d_t_.? 23, 12, 38, 375000
# t2 = d_t_.? 12, 28, 17
# t1 < t2, t1 > t2, t1 <= t2, t1 >= t2
# (False, True, False, True)
# t1 == t2, t1 != t2
# (False, True)

"""
replace ( [hour) [, minute) [, second) [, microsecond] [, tzinfo))
"""
#  - возвращает время
# с обновленными значениями. Значения можно указывать через запятую в порядке следования
# параметров или присвоить значение названюо параметра. Примеры:
# t = d_t_.? 23, 12, 38, 375000
# ?.r.. 10, 52      # Заменяем часы и минуты
# datetime.time(10, 52, 38, 375000)
# ?.r.. s.. 21   # Заменяем только секунды
# datetime.time(23, 12, 21, 375000)

"""
isoformat ()
"""
#  - возвращает время в формате ISO 8601:
# t = d_t_.? 23, 12, 38, 375000
# ?.i..
# '23:12:38.375000'

"""
strftime (<Строка формата>)
"""
#  - возвращает отформатированную строку. В строке формата
# можно указывать комбинации специальных символов, которые используются
# в функции strftime () из модуля time. Пример
# t = d_t_.? 23, 12, 38, 375000
# t.s... @ @ @
# '23:12:38'

# Тип time поддерживает такие атрибуты класса:
# + rnin - минимально возможное значение времени;
# + max - максимально возможное значение времени;
# + resolution - минимальное
# d_t_.?.mi.
# d_t_.time(0, 0)
# d_t_.?.ma.
# datetime.time(23, 59, 59, 999999)
# d_t_.?.res..
# datetime.timedelta(0, 0, 1)

# Класс datetirne из модуля datetime позволяет выполнять операции над комбинацией даты и
# времени. Конструктор класса имеет следующий формат:
# datetirne(<Гoд>, <Месяц>, <День>[, hour] [, minute] [, second]
# [, microsecond] [, tzinfo])
# Первые три параметра яв ляются обязательными. Остальные значения можно указывать
# через запяtуЮ в порядке следования параметров или присвоить значение названию параметра.
# В параметрах можно указать следующий диапазон значений:
# t <Год> - в виде числа, расположенного в диапазоне между значениями, хранящимися
# в константах MINYEAR (1) и МАХУЕАR (9999);
# t <Месяц> -число от 1 до 12 включительно;
# t <день> -число от 1 до количества дней в месяце;
# + hour-чacы (число от о до 23);
# t minute - минуты (число от о до 59);
# t second -секунды (число от о до 59);
# t microsecond-микросекунды (число от·о до 999999);
# t tzinfo -зона (экземпляр класса tzinfo или значение None).

# datetirne(<Гoд>, <Месяц>, <День>[, hour] [, minute] [, second]
# [, microsecond] [, tzinfo])
# ______ d_t_
# d_t_.d_t_ 2015, 4, 6
# datetime.d_t_(2015, 4, 6, 0, 0)
# d_t_.d_t_ 2015, 4, 6, h. 12 m.. 55
# datetime.datetime(2015, 4, 6, 12, 55)
# d_t_.d_t_ 2015, 32, 20
# ... Фрагмент опущен ...
# ValueError: month must be in 1..12
# d = d_t_.d_t_ 2015, 4, 6, 16, 1, 5
# re.. ? st. ?
# ('datetime.datetime(2015, 4, 6, 16, 1, 5)', '2015-04-06 16:01:05')

# today () - возврашает текущие дату и время:
# d_t_.d_t_.t..
# datetime.datetime(2015, 4, 6, 16, 2, 23, 944152)

"""
now ( ( <Зона> J )
"""
#  - возвращает текушие дату и время. Если параметр не задан, то метод
# аналогичен методу today r ) •
# d_t_.d_t_.n..
# datetime.datetime(2015, 4, 6, 16, 2, 45, 144777)

"""
utcnow ! )
"""
#  -возвращает текущее универсальное время (UTC):
# d_t_.d_t_.u..
# datetime.datetime(2015, 4, 6, 13, 3, 9, 862255)

"""
fromtirnestamp ( <Количество секунд> [, <Зона> J )
"""
#  - возвращает дату, соответствующую
# количеству секунд, прошедших с начала эпохи:
# ______ d_t_, ?
# d_t_.d_t_.fr..(?.ti..
# datetime.datetime(2015, 4, 6, 16, 3, 34, 978523)
# d_t_.d_t_.fr..1421579037.0
# datetime.datetime(2015, 1, 18, 14, 3, 57)

"""
utcfromtimestamp{<Koличecтвo секунд>)
"""
#  - возвращает дату, соответствующую количеству
# секунд, прошедших с начала эпохи, в универсальном времени (UTC). Примеры:
# d_t_.d_t_.? ?.ti..
# datetime.datetime(2015, 4, 6, 13, 4, 45, 756479)
# d_t_.d_t_.? 1421579037.0
# datetime.datetime(2015, 1, 18, 11, 3, 57)

"""
fromordinal (<Количество дней с 1-го года>)
"""
#  - возвращает дату, соответствующую
# количеству дней, прошедших с 1-го года. В качестве параметра указывается число от 1
# до datetirne.datetime.max. toordinal {). Примеры:
# d_t_.d_t_.ma_.too..
# # 3652059
# d_t_.d_t_.? 3652059
# # datetime.datetime(9999, 12, 31, 0, 0)
# d_t_.d_t_.? 1
# # datetime.datetime(1, 1, 1, 0, 0)

"""
combine (<Экземпляр класса oate>, <ЭкзеМПJI.яр класса tirne>)
"""
# #  - создает экземпляр
# # класса datetirne в соответствии со значениями эюемпляров классов date и tirne:
# d = d_t_.d..(2015, 4, 6)  # Экземпляр класса date
# t = d_t_.?(16, 7, 22)   # Экземпляр класса time
# d_t_.d_t_.? d, t
# # datetime.datetime(2015, 4, 6, 16, 7, 22)

"""
strptirne (<Строка с датой>, <Строка· формата>)
"""
#  - разбирает строку, указанную в первом
# # параметре, в соответствии со строкой формата. Если строка не соответствует формату,
# # возбуждается ис:кmочение ValueError.
# d_t_.d_t_.? 06.04.2015 @ @ @
# # datetime.datetime(2015, 4, 6, 0, 0)
# d_t_.d_t_.? 06.04.2015 @ @ @
# # ... Фрагмент опущен ...
# # ValueError: time data '06.04.2015'
# # does not match format '%d-%m-%Y'
# 
# # Получить результат можно с помощью следующих атрибутов:
# # + year - год (число в диапазоне от MINYEAR до МАХУЕАR);
# # + month- месяц (число от 1 до 12);
# # + dау-день (число от 1 до количества дней в месяце );
# # + hour- часы (число от о до.2з);
# # + rninute - минуты (число от о до 59);
# # second- секунды (число от о до 59);
# # + microsecond- микросекунды (число от о до 999999);
# # + tzinfo - зона (экземпляр класса tzinfo или значение None).
# d = d_t_.d_t_ 2015, 4, 6, 16, 7, 22
# ?.y.. ?.m.. ?.d..
# # (2015, 4, 6)
# ?.h.. ?.m.. ?.s.. ?.mi..
# # (16, 7, 22, 0)

# Над экземплярами класса datetime можно производить следующие операции:
# + datetirne2 = datetirnel + tirnedelta - прибавляет к дате указанный период;
# + datetirne2 = datetimel tirnedelta - вычитает из даты указанный период;
# + timedelta = datetimel datetime2 - возвращает разницу между датами;
# + можно также сравнивать две даты с помощью операторов сравнения.
# d1 = d_t_.d_t_ 2015, 4, 6, 16, 7, 22
# d2 = d_t_.d_t_ 2015, 4, 1, 12, 31, 4
# t = d_t_.t_d_ d 10, m.. 10
# d1 + t                     # Прибавляем 10 дней и 10 минут
# # d_t_.datetime(2015, 4, 16, 16, 17, 22)
# d1 — t                     # Вычитаем 10 дней и 10 минут
# # datetime.datetime(2015, 3, 27, 15, 57, 22)
# d1 — d2                    # Разница между датами
# # datetime.timedelta(5, 12978)
# d1 < d2, d1 > d2, d1 <= d2, d1 >= d2
# # (False, True, False, True)
# d1 == d2, d1 != d2
# # (False, True)
# 
# # date () - возвращает экземпляр класса date, хранящий дату:
# d = d_t_.d_t_ 2015, 4, 6, 16, 10, 54
# ?.?
# # datetime.date(2015, 4, 6)
# 
# # time <) - возвращает экземпляр класса time, хранящий время:
# d = d_t_.d_t_(2015, 4, 6, 16, 10, 54)
# ?.?
# datetime.time(16, 10, 54)

# timetz () - возвращает экземпляр класса time, хранящий время. Метод учитывает параметр
# tzinfo;
# + timestamp () - возвращает вешественное число, представляющее количество секунд,
# прошедшее с начала эпохи (обычно с 1 января 1970 г.). Поддержка этого метода появилась
# в Python 3.3.
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.?
# 1428326052.0

"""
replace
"""
# ([year] [, month] [, day) [, hour] [, minute] [, second] [, microsecond) [,
# tzinfoJ) - возвращает дату с обновленными значениями. Значения можно указывать
# через запятую в порядке следования параметров или присвоить значение названmо параметра.
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.? 2014, 12
# # datetime.datetime(2014, 12, 6, 16, 14, 12)
# ?.? h.. 12 m.. 10
# # datetime.datetime(2015, 10, 6, 12, 14, 12)

"""
timetuple ()
"""
# #  - возвращает объект struct_time с датой и временем:
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.?
# # time.struct_time(tm_year=2015, tm_mon=4, tm_mday=6, tm_hour=16, tm_min=14,
# # tm_sec=12, tm_wday=0, tm_yday=96, tm_isdst=-1)

"""
utctimetuple ()
"""
#  - возвращает объект struct_time с датой в универсальном времени
# (UTC):
# d = d_t_.d_t_(2015, 4, 6, 16, 14, 12)
# ?.?
# time.struct_time(tm_year=2015, tm_mon=4, tm_mday=6, tm_hour=16, tm_min=14,
# tm_sec=12, tm_wday=0, tm_yday=96, tm_isdst=0)

"""
toordinal ()
"""
#  - возвращает количество дней, прошедшее с 1-го года:
# d = d_t_.d_t_(2015, 4, 6, 16, 14, 12)
# ?.?
# 735694

"""
weekday()
"""
#  - возвращает порядковый номер дня в неделе (о- для понедельника, 6-
# для воскресенья):
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.? # 0 — это понедельник
# 0

"""
isoweekday()
"""
#  - возвращает порядковый номер дня в неделе (1- для понедельника,
# 7 - для воскресенья):
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.? # 1 — это понедельник
# 1

"""
isocalendar ( )
"""
#  - возвращает кортеж из трех элементов (год, номер недели в году и порядковый
# номер дня в неделе):
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.?
# (2015, 15, 1)

"""
isofoпnat ( [ <Разделитель даты и времени>] )
"""
#  - возвращает дату в формате ISO 8601.
# Если разделитель не указан, используется буква т.
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.?           # Разделитель не указан
# '2015-04-06T16:14:12'
# ?.? " "        # Пробел в качестве разделителя
# '2015-04-06 16:14:12'

# ctime () - возвращает строку формата "%а %Ь %d %Н: %М: %S %У":
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.?
# 'Mon Apr  6 16:14:12 2015'

"""
strftime (<Строка формата>)
"""
#  - возвращает отформатированную строку. В строке формата
# можно указывать комбинации специальных символов, которые используются
# в функции strftirne () из модуля tirne.
# d = d_t_.d_t_ 2015, 4, 6, 16, 14, 12
# ?.? @ @ @ @ @ @
# '06.04.2015 16:14:12'

# Модуль calendar формирует календарь в виде простого текста или НТМL-кода. Прежде чем
# использовать модуль. необходимо подключить его с помощью инструкuии:
# Модуль предоставляет с.,ед)юшие классы:
# t caler.da:: - базовый класс. который наследуют все остальные классы. Формат конструктора:

# Модуль calendar формирует календарь
# ______ ?
# c = ?.C.. 0
# c.m.d.ca. 2015, 4

# TextCalendar - позволяет вывести календарь в виде простого текста. Формат конструктора:
# TextCalendar([<Пepвый день недели>])
# c = ?.? 0
# print ?.f_y_ 2015

"""
LocaleTextCalendar
"""
#  - позволяет вывести календарь в виде простого текста. Названия
# месяцев и дней недели выводятся в соответствии с указанной локалью. Формат конструктора:
# LocaleTextCalendar([<Пepвый день недели>[, <Название локали>]])
# c = ?.? 0, Russian_Russia.1251
# print ?.f_y_ 2015

"""
HTМLCalendar
"""
#  - позволяет вывести календарь в формате НТМL. Формат конструктора:
# НТМLСаlеndаr([<Первый день недели>])
# c = ?.? 0
# print ?.f_y_ 2011

"""
LocaleHTМLCalendar
"""
#  - позволяет вывести календарь в формате HTML. Названия месяцев
# и дней недели выводятся в соответствии с указанной локалью. Формат конструктора:
# LocaleHTМLCalendar([<Пepвый день недели>[, <Название локали>)))
# c = ?.? 0 Russian_Russia.1251
# xhtml = ?.f_y_p_ 2011 en.. windows-1251
# print ?.de.. cp1251

# Text calendar output
# c = ?.? 0 Russian_Russia.1251
# c.prm_ 2015, 4, 4

# c = ?.? 0 Russian_Russia.1251
# print ?.f_y_ 2015, m=4, c=2

# c = ?.? 0 Russian_Russia.1251
# c.pry__ 2015, 2, 1, 4, 2

"""
forrnatmonth (<Год>, <Месяц> [, <True I False>] )
"""
#  - возвращает календарь на указанный
# месяц в году в виде НТМL-кода. Если в третьем параметре указано значение тrue (значение
# по умолчанию), то в заголовке таблицы после названия месяца будет указан год.
# Календарь будет отформатирован с помощью НТМL-таблиuы. Для каждой ячейки таблицы
# задается стилевой класс, с помощью которого можно управлять внешним видом
# календаря. Названия стилевых классов доступны через атрибут cssclasses, который содержит
# список названий для каждого дн.я недели:
# ______ ca..
# c = ?.HTMLC.. 0
# print ?.csscl..
# ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

# Выведем календарь на апрель 2015 года. Для будних дней укажем класс "workday", а ддя
# выходных дней- класс "week-end":
# c = ?.? 0, "Russian_Russia.1251"
# ?.csscl.. = ["workday", "workday", "workday", "workday",
#                     "workday", "week-end", "week-end"]
# print ?.f_m_ 2015, 4, F..

"""
formatyear ( <Год> [, <Количество месяцев на строке>] )
"""
#  - возвращает календарь науказанный
# год в виде НТМL-кода. Календарь будет отформатирован с помощью нескольких
# НТМL-таблиц. Для примера выведем календарь на 2015 год так, чтобы на одной
# строке выводились сразу четыре месяца:
# c = ?.? 0 Russian_Russia.1251
# print ?.f.. 2015, 4

"""
formatyearpage (<Год> [, width] [, css] [, encoding])
"""
#  - возвращает календарь на указанный
# год в виде отдельной WеЬ-страницы. Параметры имеют следующее предназначение:
# • width- количество месяцев на строке (по умолчанию з);
# • css - название файла с таблицей стилей (по умолчанию "calendar. css");
# • encoding- кодировка файла. Название кодировки будет указано в параметре
# encoding ХМL-пролога, а также в теге <meta>.
# Значения можно указывать через запятую в порядке следования параметров или присвоить
# значение названию параметра. Для примера выведем календарь на 2015 год так,
# чтобы на одной строке выводилось сразу четыре месяца. Укажем при этом кодировку
# файла:
# c = ?.? 0 Russian_Russia.1251
# xhtml = ?.?(2015, 4, en.._windows-1251
# ty.. ? # Возвращаемая строка имеет тип данных bytes
# <class 'bytes'>
# print ?.de.. cp1251

"""
setfirstweekday ( <Первый день недели>)
"""
#  - устанавливает первый день недели для календаря.
# В качестве параметра указывается число от о (для понедельника) до 6 (для воскресенья).
# Вместо чисел можно использовать встроенные константы MONDAY, TUESDAY,
# WEDNESDAY, THURSDAY, FRIDAY, SATURDAY или SUNDAY. Получить текущее значение параметра
# можно с помощью функции firstweekday (). Установим воскресенье первым днем недели:
# ______ ca..
# ?.?    # По умолчанию 0
# 0
# ?.s_? 6 # Изменяем значение
# ?.?     # Проверяем установку
# 6

"""
month (<Год>, <Месяц> [ , <Ширина поля с днем> [ , <Кот1чество символов перевода строки>
"""
# 
# J J J - возвращает текстовый календарь на указанный месяц в году. Третий параметр
# позволяет указать ширину поля с днем, а четвертый параметр - количество символов
# перевода строки между строками. Выведем календарь на апрель 2015 года:
# ?.s_f_ 0
# print ?.? 2015, 4


"""
prmonth (<Год>, <Месяu> [, <Ширина поля с днем> [, <Ко.m1чество Cl п-1Волов перевода
# строки> J J )
"""
#  - функция аналогична функции mon,:r, ( ) , но не возвращает календарь в виде
# строки, а сразу выводит его. Выведем календарь на апрель 2015 года:
# ?.? 2015, 4


"""
monthcalendar (<Год>, <Месяц>)
"""
#  - возвращает двумерный список всех дней в указанном
# месяце, распределенных по дням недели. Дни, выходящие за пределы месяца, будут
# представлены нулями. Выведем массив для апреля 2015 года:
# ?.? 2015, 4

"""
monthrange (<Год>, <Месяu>)
"""
#  - возвращает кортеж из двух элементов: номера дня недели,
# приходящегося на первое число указанного месяца, и количества дней в месяце:
# print ?.? 2015, 4

# calendar ( <Год> [, w J [, 1 J [, с J [, m] ) - возвращает текстовый календарь на указанный
# год. Параметры имеют следующее предназначение:
# • w - ширина поля с днем ( по умолчанию 2 );
# • 1- количество символов перевода строки между строками (по умолчанию 1);
# • с - количество пробелов между месяцами (по умолчанию 6);
# • m- количество месяцев на строке (по умолчанmо 3).
# Значения можно указывать через запятую в порядке следования параметров или присвоить
# значение названию параметра. Дnя примера выведем календарь на 2015 год так, чтобы
# на одной строке выводилось сразу четыре месяца. У становим при этом количество
# пробелов между месяцами:
# print ?.? 2015, m=4, c=2

"""
рrсаl(<Год>[, w] [, 1] [, с][, m])
"""
#  -функция аналогична функции calendar(), но не
# возвращает календарь в виде строки, а сразу выводит его. Для примера выведем календарь
# на 2015 год по два месяца на строке. Расстояние между месяцами установим равным
# 4 символам, ширину поля с датой равной 2 символам, а строки разделим одним
# символом перевода строки:

# ?.?  2015, 2, 1, 4, 2

"""
weekheader (<n>)
"""
#  - возвращает строку, которая содержиr аббревиаl)'Ры дней недели с учетом
# текущей локали, разделенные пробелами. Единственный параметр задает длину каждой аббре­
# вюпуры в символах.
# ?.? 4
# 'Mon  Tue  Wed  Thu  Fri  Sat  Sun '
# ?.? 2
# 'Mo Tu We Th Fr Sa Su'
# ______ lo__                 # Задаем другую локаль
# lo__.s_l_ lo__.L_A. Russian_Russia.1251
# 'Russian_Russia.1251'
# ?.? 2

"""
isleap (<Год>)
"""
#  - возвращает значение тrue, если указанный год является високосным,
# в противном случае - False:

# ?.? 2015 ?.? 2012

"""
leapdays (<Годl>, <Год2>)
"""
#  - возвращает количество високосных лет в диапазоне
# от <Годl> до <Год2> ( <Год2> не учитывается):
# ?.? 2010, 2012 # 2012 не учитывается
# # 0
# ?.? 2010, 2015 # 2012 — високосный год
# # 1
# ?.? 2010, 2017 # 2012 и 2016 — високосные года
# # 2

"""
weekday(<Гoд>, <Месяц>, <день>)
"""
#  - возвращает номер дн.я недели (о- для понедельника,
# 6 - для воскресенья):
# ?.weekday(2015, 4, 7)
# 1

# timegm(<OOьeкт struct_time>) - возвращает число, представляющее количество секунд,
# прошедших с начала эпохи. В качестве параметра указывается объект struct_time
# с датой и временем, возвращаемый функцией gmtime () из модуля tirne.
# ______ ca.., ?
# d = ?.gm..(1321954972.0) # Дата 22-11-2011
# d
# # time.struct_time(tm_year=2011, tm_mon=11, tm_mday=22, tm_hour=9,
# #  tm_min=42, tm_sec=52, tm_wday=1, tm_yday=326, tm_isdst=0)
# tu..(d)
# # (2011, 11, 22, 9, 42, 52, 1, 326, 0)
# ?.?(d)
# # 1321954972
# ?.? 2011, 11, 22, 9, 42, 52, 1, 326, 0
# # 1321954972

"""
day_name
"""
#  - список полных названий дней недели в текущей локали:
# [i ___ ? __ ?.?

"""
сtау_аььr -
"""
#  список аббревиатур названий дней недели в текущей локали:
# i ___ i __ ?.?

"""
month- name -
"""
#  список полных названий месяцев в текyшей лакали:
# i ___ i __ ?.?

"""
month_abbr -
"""
#  список аббревиатур названий месяцев в текущей лакали
# i ___ i __ ?.?

# Настройка локали
# day_abbr
# month_name
# month_abbr
# ______ lo__ # Настройка локали
# lo__.s_l_ lo__.L_A.. Russian_Russia.1251
# 'Russian_Russia.1251'
#  i ___ i __ ?.d_a..
# ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# i ___ i __ ?.m._n.
# ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
#  'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# i ___ i __ ?.m_a..
# ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен',
#  'окт', 'ноя', 'дек']

# Runtime measurement
# -*- coding: utf-8 -*-
# ____ t_i_ ______ T..
# code1 = """\
# i, j = 1, 0
# w.. i < 10001
#     j +_ i
#     i +_ 1
# """
# t1 = T.. stmt_?
# print("while:", ?.t_i_ nu.._10000
# code2 = """\
# j = 0
# ___ i __ ra.. 1, 10001
#     j +_ i
# """
# t2 = T.. stmt_?
# print("for:", ?.t.i. nu.._10000
# code3 = """\
# j = su. ra.. 1, 10001
# """
# t3 = T.. stmt_?
# print("sum:", ?.t_i_ nu.._10000
# input()
# 
# Модуль timeit позволяет измерить время выполнения небольших фрагментов кода с целью
# оптимизации программы. Прежде чем использовать модуль, необходимо подключить его с
# помощью инструкции:
# ____ t_i_ ______ T..
# 
# # Измерения производятся с помощью класса Timer. Конструктор класса имеет следующий
# # формат:
# T.. stmt_ pass [, setup_pass [, timer_<timer function>
# 
# # В параметре stmt указывается код (в виде строки), время выполнения которого предполагается
# # измерить. Параметр setup позволяет указать код, который будет выполнен перед измерением
# # времени выполнения кода в параметре stmt. Например, в параметре setup можно
# # подключить модуль.
# # Получить время выполнения можно с помощью метода timeit ( [numЬer= 1000000]). В параметре
# # numЬer указывается количество повторений. Для примера просуммируем числа от 1
# # до 10000 тремя способами и выведем время выполнения каждого способа
# 
# # Метод repeat ( [repeat= ЗJ [, nurnЬer= lOOOOOOJ) вызывает метод timeit () указанное количество
# # раз (задается в параметре repeat) и возвращает список значений. Аргумент nu
# # -*- coding: utf-8 -*-
# ____ t_i_ ______ T..
# code1 = """\
# arr1       # list 
# ___ i __ ra.. 1, 10001
#     ?.ap.. str ?
# """
# t1 = T.. stmt_?
# print("append:", ?.re.. r.._3 nu.._2000
# code2 = """\
# arr2 = str(i) ___ ? __ ra..1 10001
# """
# t2 = T.. stmt_?
# print("генератор:", ?.re.. re.._3 nu.. 2000
# input()
# 
# # Cоздаем объектf datetime
# timestamp = d_t_.d_t_ 2015, 7, 17, 12, 30, 45
# print ?
# 
# now = d_t_.d_t_.?
# print ?
# print (?.y.. ?.m.. ?.d..
# print (?.h.. ?.m.. ?.s..
# print (?.microsecond)
# 
# # Количество дней, прошедших с 01.01.1970
# print ?.t..
# 
# # Время в секундах с начала эпохи.
# print ?.t..
# # День недели в виде чис
# 
# # # День недели в виде числа, понедельник - 0, воскресенье - 6.
# print ?.w..
# 
# # День недели в виде числа, понедельник - 1, воскресенье - 7.
# print(?.i_w_d_
# 
# # ортеж (year, week number, weekday).
# print ?.is..
# 
# # # Строка вида "YYYY-MM-DD HH:MM:SS.mmmmmm", если microsecond == 0, "YYYY-MM-DD HH:MM:SS".
# # # Параметр является разделителем между датой и временем
# print ?.is.. ' '
# 
# day = d_t_.d..(2015, 7, 18)
# ___ i in day.timetuple():
#     # первые три числа в кортеже: год, месяц и число.  Последние 2 (не считая -1) -
#     # день недели (понедельник - 0) и номер дня от начала года
#     print(i)
# 
# print(?.is..
# print(?.str.. @ @ @     # day|month|year
# print(?.str.. @ @ @ @  # название дня недели в зависимости от настроек|day|название месяца в зависимости от настроек локали|year
# print('@1 is @ __, @ is @ __.'.f.. d.. "day", "month"
