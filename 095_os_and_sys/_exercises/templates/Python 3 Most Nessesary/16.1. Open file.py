# # # -*- coding: utf-8 -*-
#
# # Прежде чем работать с файлом, необходимо создать объект файла с помощью функции
# # open ( ) .
# #
# # В первом параметре указывается путь к файлу. Путь может быть абсолютным или относительным.
# # При указании абсолютного пути в Windows следует учитывать, что в Python слеш
# # является специальным символом. По этой причине слеш необходимо удваивать или вместо
# # обычных строк использовать неформатированные строки.
#
# # "C:\\temp\\new\\file.txt"    # Правильно
# # 'C:\\temp\\new\\file.txt'
# # r"C:\temp\new\file.txt"      # Правильно
# # 'C:\\temp\\new\\file.txt'
# # "C:\temp\new\file.txt"       # Неправильно!!!
# # 'C:\temp\new\x0cile.txt'
#
#
# # open("C:\temp\new\file.txt")
# # Traceback (most recent call last):
# #   File "<pyshell#0>", line 1, in <module>
# #     open("C:\temp\new\file.txt")
# # OSError: [Errno 22] Invalid argument: 'C:\temp\new\x0cile.txt'
#
# # если открываемый файл находится в текущем рабочем каталоге, то можно указать только
#
# # название файла.
#
# ______ __.pa__ # Подключаем модуль
# # Файл в текущем рабочем каталоге (C:\book\)
# print __.pa__.a.p. _"file.txt"
# # 'C:\\book\\file.txt'
# # ######################################################################################################################
#
# # если открываемый файл расположен во вложенной папке, то перед названием файла приводятся
# # названия вложенных папок через слеш.
#
# # Открываемый файл в C:\book\folder1\
# print __.pa__.a.p. _"folder1/file.txt"
# # 'C:\\book\\folder1\\file.txt'
# # ######################################################################################################################
#
# # Открываемый файл в C:\book\folder1\folder2\
# print __.pa__.a.p. _"folder1/folder2/file.txt"
# # 'C:\\book\\folder1\\folder2\\file.txt'
# # ######################################################################################################################
#
# # если папка с файлом расположена ниже уровнем, то перед названием файла указываются
# # две точки и слеш (" .. /").
#
# # Открываемый файл в C:\
# print __.pa__.a.p. _"../file.txt"
# # 'C:\\file.txt'
# # ######################################################################################################################
#
# # если в начале пути расположен слеш, то путь отсчитывается от корня диска. В этом случае
# # местоположение текущего рабочего каталога не имеет значения.
#
# # Открываемый файл в C:\book\folder1\
# print __.pa__.a.p. _"/book/folder1/file.txt"
# # 'C:\\book\\folder1\\file.txt'
# # ######################################################################################################################
#
# # Открываемый файл в C:\book\folder1\folder2\
# print __.pa__.a.p. _"/book/folder1/folder2/file.txt"
# # 'C:\\book\\folder1\\folder2\\file.txt'
# # ######################################################################################################################
#
# # Как можно видеть, в абсолютном и относительном путях можно указать как прямые, так и
# # обратные слеши. Все они будут автоматически преобразованы с учетом значения атрибута
# # sep и:з модуля os. path. Значение этого атрибута зависит от используемой операционной
# # системы. Выведем значение атрибута sep в операционной системе Windows:
#
# print __.pa__.se.
# # '\\'
# # ######################################################################################################################
#
# print __.pa__.a.p. _"C:/book/folder1/file.txt"
# # 'C:\\book\\folder1\\file.txt'
# # ######################################################################################################################