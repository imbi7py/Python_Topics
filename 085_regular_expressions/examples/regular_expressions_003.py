# Что такое регулярные выражения и как их использовать?
#
# Говоря простым языком, регулярное выражение — это последовательность символов, используемая для поиска и замены текста в строке или файле. Как уже было упомянуто, их поддерживает множество языков общего назначения: Python, Perl, R. Так что изучение регулярных выражений рано или поздно пригодится.
#
# Регулярные выражения используют два типа символов:
#
#     специальные символы: как следует из названия, у этих символов есть специальные значения. Аналогично символу *, который как правило означает «любой символ» (но в регулярных выражениях работает немного иначе, о чем поговорим ниже);
#     литералы (например: a, b, 1, 2 и т. д.).
#
# В Python для работы с регулярными выражениями есть модуль re. Для использования его нужно импортировать:
#
# import re
#
# Чаще всего регулярные выражения используются для:
#
#     поиска в строке;
#     разбиения строки на подстроки;
#     замены части строки.
#
# Давайте посмотрим на методы, которые предоставляет библиотека re для этих задач. Вот наиболее часто используемые из них:
#
#     re.match()
#     re.search()
#     re.findall()
#     re.split()
#     re.sub()
#     re.compile()
#
# Рассмотрим их подробнее.

# re.match(pattern, string):
#
# Этот метод ищет по заданному шаблону в начале строки. Например, если мы вызовем метод match() на строке «AV Analytics AV» с шаблоном «AV», то он завершится успешно. Однако если мы будем искать «Analytics», то результат будет отрицательный. Давайте посмотрим на его работу:
#
# import re
# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print result
#
# Результат:
# <_sre.SRE_Match object at 0x0000000009BE4370>
#
# Искомая подстрока найдена. Чтобы вывести ее содержимое, используем метод group(). (Мы используем «r» перед строкой шаблона, чтобы показать, что это «сырая» строка в Python).
#
# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print result.group(0)
#
# Результат:
# AV
#
# Теперь попробуем найти «Analytics» в данной строке. Поскольку строка начинается на «AV», метод вернет None:
#
# result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
# print result
#
# Результат:
# None
#
# Также есть методы start() и end() для того, чтобы узнать начальную и конечную позицию найденной строки.
#
# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print result.start()
# print result.end()
#
# Результат:
# 0
# 2
#
# Эти методы иногда очень полезны для работы со строками.

# re.search(pattern, string):
#
# Этот метод похож на match(), но он ищет не только в начале строки. В отличие от предыдущего, search() вернет объект, если мы попытаемся найти «Analytics».
#
# result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
# print result.group(0)
#
# Результат:
# Analytics
#
# Метод search() ищет по всей строке, но возвращает только первое найденное совпадение.
# re.findall(pattern, string):
#
# Этот метод возвращает список всех найденных совпадений. У метода findall() нет ограничений на поиск в начале или конце строки. Если мы будем искать «AV» в нашей строке, он вернет все вхождения «AV». Для поиска рекомендуется использовать именно findall(), так как он может работать и как re.search(), и как re.match().
#
# result = re.findall(r'AV', 'AV Analytics Vidhya AV')
# print result
#
# Результат:
# ['AV', 'AV']
#
# re.split(pattern, string, [maxsplit=0]):
#
# Этот метод разделяет строку по заданному шаблону.
#
# result = re.split(r'y', 'Analytics')
# print result
#
# Результат:
# ['Anal', 'tics']
#
# В примере мы разделили слово «Analytics» по букве «y». Метод split() принимает также аргумент maxsplit со значением по умолчанию, равным 0. В данном случае он разделит строку столько раз, сколько возможно, но если указать этот аргумент, то разделение будет произведено не более указанного количества раз. Давайте посмотрим на примеры:
#
# result = re.split(r'i', 'Analytics Vidhya')
# print result
#
# Результат:
# ['Analyt', 'cs V', 'dhya'] # все возможные участки.
#
# result = re.split(r'i', 'Analytics Vidhya',maxsplit=1)
# print result
#
# Результат:
# ['Analyt', 'cs Vidhya']
#
# Мы установили параметр maxsplit равным 1, и в результате строка была разделена на две части вместо трех.

# re.sub(pattern, repl, string):
#
# Этот метод ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной.
#
# result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# 'AV is largest Analytics community of the World'
#
# re.compile(pattern, repl, string):
#
# Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.
#
# pattern = re.compile('AV')
# result = pattern.findall('AV Analytics Vidhya AV')
# print result
# result2 = pattern.findall('AV is largest analytics community of India')
# print result2
#
# Результат:
# ['AV', 'AV']
# ['AV']
#
# До сих пор мы рассматривали поиск определенной последовательности символов. Но что, если у нас нет определенного шаблона, и нам надо вернуть набор символов из строки, отвечающий определенным правилам? Такая задача часто стоит при извлечении информации из строк. Это можно сделать, написав выражение с использованием специальных символов. Вот наиболее часто используемые из них:
# Оператор 	Описание
# . 	Один любой символ, кроме новой строки \n.
# ? 	0 или 1 вхождение шаблона слева
# + 	1 и более вхождений шаблона слева
# * 	0 и более вхождений шаблона слева
# \w 	Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d 	Любая цифра [0-9] (\D — все, кроме цифры)
# \s 	Любой пробельный символ (\S — любой непробельный символ)
# \b 	Граница слова
# [..] 	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \ 	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $ 	Начало и конец строки соответственно
# {n,m} 	От n до m вхождений ({,m} — от 0 до m)
# a|b 	Соответствует a или b
# () 	Группирует выражение и возвращает найденный текст
# \t, \n, \r 	Символ табуляции, новой строки и возврата каретки соответственно
#
#
#
# Больше информации по специальным символам, таким как (), | и др., можно найти на странице документации: https://docs.python.org/2/library/re.html).
#
# Теперь давайте посмотрим на примеры использования регулярных выражений.

# Примеры использования регулярных выражений
# Задача 1: Вернуть первое слово из строки
#
# Сначала попробуем вытащить каждый символ (используя .)
#
# result = re.findall(r'.', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['A', 'V', ' ', 'i', 's', ' ', 'l', 'a', 'r', 'g', 'e', 's', 't', ' ', 'A', 'n', 'a', 'l', 'y', 't', 'i', 'c', 's', ' ', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', ' ', 'o', 'f', ' ', 'I', 'n', 'd', 'i', 'a']
#
# Для того, чтобы в конечный результат не попал пробел, используем вместо . \w.
#
# result = re.findall(r'\w', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['A', 'V', 'i', 's', 'l', 'a', 'r', 'g', 'e', 's', 't', 'A', 'n', 'a', 'l', 'y', 't', 'i', 'c', 's', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', 'o', 'f', 'I', 'n', 'd', 'i', 'a']
#
# Теперь попробуем достать каждое слово (используя * или +)
#
# result = re.findall(r'\w*', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV', '', 'is', '', 'largest', '', 'Analytics', '', 'community', '', 'of', '', 'India', '']
#
# И снова в результат попали пробелы, так как * означает «ноль или более символов». Для того, чтобы их убрать, используем +:
#
# result = re.findall(r'\w+', 'AV is largest Analytics community of India')
# print result
# Результат:
# ['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India']
#
# Теперь вытащим первое слово, используя ^:
#
# result = re.findall(r'^\w+', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV']
#
# Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:
#
# result = re.findall(r'\w+$', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# [‘India’]
#
# Задача 2: Вернуть первые два символа каждого слова
#
# Вариант 1: используя \w, вытащить два последовательных символа, кроме пробельных, из каждого слова:
#
# result = re.findall(r'\w\w', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV', 'is', 'la', 'rg', 'es', 'An', 'al', 'yt', 'ic', 'co', 'mm', 'un', 'it', 'of', 'In', 'di']
#
# Вариант 2: вытащить два последовательных символа, используя символ границы слова (\b):
#
# result = re.findall(r'\b\w.', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV', 'is', 'la', 'An', 'co', 'of', 'In']
#
# Задача 3: вернуть список доменов из списка адресов электронной почты
#
# Давайте снова рассмотрим решение пошагово. Сначала вернем все символы после «@»:
#
# result = re.findall(r'@\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print result
#
# Результат:
# ['@gmail', '@test', '@analyticsvidhya', '@rest']
#
# Как видим, части «.com», «.in» и т. д. не попали в результат. Изменим наш код:
#
# result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print result
#
# Результат:
# ['@gmail.com', '@test.in', '@analyticsvidhya.com', '@rest.biz']
#
# Второй вариант — вытащить только домен верхнего уровня, используя группировку — ( ):
#
# result = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print result
#
# Результат:
# ['com', 'in', 'com', 'biz']
#
# Задача 4: Извлечь дату из строки
#
# Используем \d для извлечения цифр.
#
# result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print result
#
# Результат:
# ['12-05-2007', '11-11-2011', '12-01-2009']
#
# Для извлечения только года нам опять помогут скобки:
#
# result = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print result
#
# Результат:
# ['2007', '2011', '2009']
#
# Задача 5: Извлечь все слова, начинающиеся на гласную
#
# Для начала вернем все слова:
#
# result = re.findall(r'\w+', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India']
#
# А теперь — только те, которые начинаются на определенные буквы (используя []):
#
# result = re.findall(r'[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV', 'is', 'argest', 'Analytics', 'ommunity', 'of', 'India']
#
# Выше мы видим обрезанные слова «argest» и «ommunity». Для того, чтобы убрать их, используем \b для обозначения границы слова:
#
# result = re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['AV', 'is', 'Analytics', 'of', 'India']
#
# Также мы можем использовать ^ внутри квадратных скобок для инвертирования группы:
#
# result = re.findall(r'\b[^aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# [' is', ' largest', ' Analytics', ' community', ' of', ' India']
#
# В результат попали слова, «начинающиеся» с пробела. Уберем их, включив пробел в диапазон в квадратных скобках:
#
# result = re.findall(r'\b[^aeiouAEIOU ]\w+', 'AV is largest Analytics community of India')
# print result
#
# Результат:
# ['largest', 'community']
#
# Задача 6: Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9)
#
# У нас есть список телефонных номеров, и нам нужно проверить их, используя регулярные выражения:
#
# li = ['9999999999', '999999-999', '99999x9999']
#
# for val in li:
#     if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
#         print 'yes'
#     else:
#         print 'no'
#
# Результат:
# yes
# no
# no
#
# Задача 7: Разбить строку по нескольким разделителям
#
# Возможное решение:
#
# line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
# result = re.split(r'[;,\s]', line)
# print result
#
# Результат:
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
#
# Также мы можем использовать метод re.sub() для замены всех разделителей пробелами:
#
# line = 'asdf fjdk;afed,fjek,asdf,foo'
# result = re.sub(r'[;,\s]',' ', line)
# print result
#
# Результат:
# asdf fjdk afed fjek asdf foo
#
# Задача 8: Извлечь информацию из html-файла
#
# Допустим, нам надо извлечь информацию из html-файла, заключенную между <td> и </td>, кроме первого столбца с номером. Также будем считать, что html-код содержится в строке.
#
# Пример содержимого html-файла:
#
# 1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily
#
# Решение (если поместить содержимое файла в переменную test_str):
#
# result = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', test_str)
# print result
#
# Результат:
# [('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'), ('Ethan', 'Mia'), ('Michael', 'Emily')]
#
# Заключение

# В этой статье мы узнали, что такое регулярные выражения и как их использовать, на примере библиотеки re в Python. Кроме того, мы рассмотрели наиболее часто встречающиеся задачи, в которых их можно применить.