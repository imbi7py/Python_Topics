# # -*- coding: utf-8 -*-
# 
# # Если в параметре <Модификатор> указан флаг м (или МULTILINE), то поиск производится
# # в строке, состоящей из неско�ъких подстрок, разделенных символом новой строки (\n).
# # В этом случае символ " соответствует привязке к началу каждой подстроки, а символ $ -
# # позиции перед символом перевода строки (листинг 7 .2).
# 
# # _______ __
# #
# # p = __.c.. _ 1? .2? 3?       # Точка не соответствует \n  # # 1.Starts with | 2.One or more occurrences | 3.Ends with |
# # ?.f..("str1\nstr2\nstr3") # Ничего не найдено
# # # []
# # ? = __.c.. _ 1? .2? 3?  __.S # Теперь точка соответствует \n #1. Starts with | 2.One or more occurrences | 3. Ends with | Makes a period (dot) match any character, including a newline.
# # ?.f..("str1\nstr2\nstr3") # Строка полностью соответствует
# # # ['str1\nstr2\nstr3']
# # ? = __.c.. _ 1? .2? 3?  __.4? # 4.Многострочный режим          # 1.Starts with | 2.One or more occurrences | 3.Ends with |
# # ?.f..("str1\nstr2\nstr3") # Получили каждую подстроку
# # # ['str1', 'str2', 'str3']
