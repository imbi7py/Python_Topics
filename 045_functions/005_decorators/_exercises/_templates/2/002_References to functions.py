# -*- coding: utf-8 -*-

# ___ shout word _ да
#     r_ ?.ca__ + !
#
#
# print shout
# # выведет: 'Да!'
#
# # Так как функция - это объект, вы связать её с переменнной,
# # как и любой другой объект
# scream _ ?
#
# # Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# # мы связываем её с переменной "scream". Это означает, что теперь мы
# # можем вызывать "shout" через "scream":
#
# print scream
# # выведет: 'Да!'
#
# # Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# # будет доступна через переменную "scream"
#
# del shout
# t_
#     print shout
# ____ N... __ e
#     print ?
#     # выведет: "name 'shout' is not defined"
#
# print s..
# # выведет: 'Да!'
#
# # Запомним этот факт, скоро мы к нему вернёмся, но кроме того, стоит понимать, что функция в Python'e может быть
# # определена… внутри другой функции!
#
# ___ talk
#     # Внутри определения функции "talk" мы можем определить другую...
#     __ whisper word _ да
#         r_ ?.lo__ + ...
#
#     # ... и сразу же её использовать!
#     print ?
#
#
# # Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем
# # и вызывается функция "whisper".
# ?
# # выведет: "да..."
#
# # Но вне функции "talk" НЕ существует никакой функции "whisper":
# # try:
# # #     print(whisper())
# # # except NameError as e:
# # #     print(e)
# # #     # выведет : "name 'whisper' is not defined"
# # Теперь мы знаем, что функции являются полноправными объектами, а значит:
# #
# #     могут быть связаны с переменной;
# #     могут быть определены одна внутри другой.
# #
# #
# # Что ж, а это значит, что одна функция может вернуть другую функцию!
#
# ___ getTalk type _ shout
#     # Мы определяем функции прямо здесь
#     ___ shout word_ да
#         r_ ?.ca__ + !
#
#     ___ whisper word _ да
#         r_ ?.lo__ + ...
#
#     # Затем возвращаем необходимую
#     __ ty.. __  sh..
#         # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
#         # а вернуть объект функции
#         r_ sh..
#     ____
#         r_ w...
#
#
# # Как использовать это непонятное нечто?
# # Возьмём функцию и свяжем её с переменной
# talk _ ?
#
# # Как мы можем видеть, "talk" теперь - объект "function":
# print talk
# # выведет: <function shout at 0xb7ea817c>
#
# # Который можно вызывать, как и функцию, определённую "обычным образом":
# print ?
#
# # Если нам захочется - можно вызвать её напрямую из возвращаемого значения:
# print ? wh..
# # выведет: да...
#
# # Подождите, раз мы можем возвращать функцию, значит, мы можем и передавать её другой функции, как параметр:
#
# ___ doSomethingBefore func
#     print Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
#     print ?
#
# ? scream
# # выведет:
# # Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# # Да!
#
# # Ну что, теперь у нас есть все необходимые знания для того, чтобы понять, как работают декораторы.
# # Как вы могли догадаться, декораторы — это, по сути, просто своеобразные «обёртки», которые дают нам возможность
# # делать что-либо до и после того, что сделает декорируемая функция, не изменяя её.
