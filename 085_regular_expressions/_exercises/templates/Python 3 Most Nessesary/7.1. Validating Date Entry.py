# # -*- coding: utf-8 -*-

# Внутри регулярного выражения символы . ", $, *, +, ?, {, [, ], \, 1, (и) имеют специальное
# значение. Если эти символы должны трактоваться как есть, их следует экранировать с помощью слеша.
# Некоторые специальные символы теряют свое особое значение, если их разместить внутри квадратных скобок, -
# в этом случае экранировать их не нужно. Например,
# как уже бьmо отмечено ранее, метасимвол «точка» по умолчанию соответствует любому
# символу, кроме символа перевода строки. Если необходимо найти именно точку, то перед
# точкой нужно указать символ \ или разместить точку внутри квадратных скобок: [ . J •

# _______ __         # Подключаем модуль
#
# d = "29,12.2009"  # Вместо точки указана запятая
#
# p = __.c.. _ 1? 0-3 0-9 ? 01 0-9 ? 12 09 0-9 0-9 2?     # 1.Starts with |  2.Ends with
# # Символ "\" не указан перед точкой
# __ ?.s..
# print("Дата введена правильно")
# ____
#     print("Дата введена неправильно")
# # Так как точка означает любой символ,
# # выведет: Дата введена правильно
#
# p = __.c.. _ 1? 0-3  0-9 2_? 01  0-9 2_? 12  09  0-9  0-9 3?  # 1.Starts with | 2. ekranirovat' |3. Ends with
# # Символ "\" указан перед точкой
# __ ?.s.. ?
#     print("Дата введена правильно")
# ____
#     print("Дата введена неправильно")
# # Так как перед точкой указан символ "\",
# # выведет: Дата введена неправильно
#
# p = __.c.. 1? 0-3  0-9  |?  01  0-9  |?  12  09  0-9  0-9 2?   # 1.Starts with | 2.Ends with
# # Точка внутри квадратных скобок
# __ ?.s.. ?
#     print("Дата введена правильно")
# ____
#     print("Дата введена неправильно")
# # Выведет: Дата введена неправильно
# input()

#  В этом примере мы осуществляли привязку к началу и концу строки с помощью следующих
# метасимволов:
# t " - привязка к началу строки или подстроки. Она зависит от флагов м (или МULTILINE)
# И S (ИЛИ DOТALL);
# t $ - привязка к концу строк.и или подстроки. Она зависит от флагов м (или МULTILINE)
# И S (ИЛИ DOТALL);
# t \А - привязка к началу строк.и (не зависит от модификатора);
# t \Z - привязка к концу строки (не зависит от модификатора).

# Если в параметре <Модификатор> указан флаг м (или МULTILINE), то поиск производится
# в строке, состоящей из неско�ъких подстрок, разделенных символом новой строки (\n).
# В этом случае символ " соответствует привязке к началу каждой подстроки, а символ $ -
# позиции перед символом перевода строки (листинг 7 .2).
