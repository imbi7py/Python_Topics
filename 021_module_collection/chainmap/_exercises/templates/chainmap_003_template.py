# # -*- coding: utf-8 -*-
#
# # ChainMap
# #
# # ChainMap – это класс, который дает возможность объединить несколько сопоставлений вместе таким образом, чтобы они
# # стали единым целым. Если вы обратитесь к документации, то увидите, что данный класс принимает **maps*.
#
# # Это значит, что ChainMap будет принимать любое количество сопоставлений или словарей и превращать их в
# # единое обновляемое представление. Давайте взглянем на пример, чтобы вы могли увидеть, как это работает:
#
# f__ c.. _______ C..
#
# car_parts _
#     'hood': 500,
#     'engine': 5000,
#     'front_door': 750
#
#
# car_options _
#     'A/C': 1000,
#     'Turbo': 2500,
#     'rollbar': 300
#
#
# car_accessories _
#     'cover': 100,
#     'hood_ornament': 150,
#     'seat_cover': 99
#
#
# car_pricing _ C...(c.._a.. c.._o.. c.._p.
#
# print c._p.. 'hood' # 500
#
# # Здесь мы импортировали ChainMap из модуля collections. Затем мы создали три словаря Python.
# # Далее, мы создали экземпляр ChainMap, передав эти три словаря. В конце мы попытались получить доступ к одному из
# # ключей в нашем ChainMap. После этого, ChainMap пройдет через каждое сопоставление, чтобы увидеть, существует ли
# # данный ключ и имеет ли он значение. Если это так, тогда ChainMap вернет первое найденное значение,
# # которое соответствует ключу. Это весьма полезно в тех случаях, когда вам нужно установить настройки по умолчанию.
# #
# # Давайте представим, что нам нужно создать приложение, которое имеет определенные настройки по умолчанию.
# # Приложение также будет знать о переменных среды операционной системы. Если существует переменная среды,
# # которая соответствует значению ключа, который расположен в нашем приложении по умолчанию, тогда среда переопределит
# # наши настройки по умолчанию. Теперь давайте представим, что мы можем передавать аргументы нашему приложению.
# # Эти аргументы имеют преимущество над средой и настройками по умолчанию. Это тот случай,
# # когда ChainMap представлен во всей красе. Давайте взглянем на пример, который основан на документации Python:
#
# _______ arg..
# _______ o.
#
# f.. c.. _______ C...
#
#
# ___ main
#     app_defaults _  'username' 'admin' 'password' 'admin'
#
#     parser _ arg__.A..P..
#     p__.a.._arg.. '-u' '--username'
#     p__.add_arg.. '-p' '--password'
#     args _ p__.p.._a..
#
#     command_line_arguments _
#         key value ___ k.. v.. i_ va.. ar__.it.. i_ va..
#     }
#
#     chain _ C..(
#         c._l._a.
#         o_.e..
#         a.._d..
#     )
#
#     print c.. 'username'
#
#
# __ ____ __ _____
#     m..
#     o_.e... 'username' _ 'test'
#     m..
#
# # Давайте немного притормозим. Здесь мы импортировали модуль Python argparse совместно с модулем os.
# # Мы также импортировали ChainMap.Next, простую функцию со слегка нелепыми настройками. Я видел, что эти настройки
# # используются в некоторых популярных роутерах. Далее, мы устанавливаем наш парсер аргументов, и указываем ему,
# # как именно он будет обрабатывать определенные параметры командной строки. Обратите внимание на то, что argparse
# # не предоставляет способ получения объектов словаря или его аргументов, так что мы используем dict для извлечения
# # того, что нам нужно. Здесь мы задействуем встроенный инструмент Python vars. Если вы вызовете его без аргументов,
# # то vars будет вести себя как встроенный locals. Но если передать его объекту, то vars будет выступать в роли
# # эквивалента свойству объекта __dict__. Другими словами, vars(args) равен args.__dict__. В конце мы создаем наш
# # ChainMap, передав аргументы нашей командной строке (если таковые имеются), затем переменные среды и, наконец,
# # настройки. В конце кода, мы пытаемся вызвать нашу функцию, затем устанавливаем переменные среды и снова делаем вызов.
# # Запустите его и увидите, что в выдаче будет admin, и, как и ожидалось, test. Теперь попробуем вызвать скрипт
# # с аргументом командной строки:
#
# # python chain_map.py -u mike
#
# # После запуска кода, я получил mike дважды. Это связанно с тем, что аргумент нашей командной строки переопределяет
# # все остальное. Не важно, что мы установили среду, так как наш ChainMap смотрит на аргументы командной строки
# # в первую очередь, затем на все остальное. Теперь вы знаете, как использовать ChainMaps, так что мы можем перейти к
# # Counter!