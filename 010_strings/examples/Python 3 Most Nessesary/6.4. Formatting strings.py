# -*- coding: utf-8 -*-

print("%s" % 10)                         # Один элемент
# '10'
print("%s — %s — %s" % (10, 20, 30))     # Несколько элементов
'10 — 20 — 30'


print("%(name)s — %(year)s" % {"year": 1978, "name": "Nik"})
# 'Nik — 1978'


print("%#o %#o %#o" % (0o77, 10, 105))
# 0o77 0o12 0o12
print("%#x %#x %#x" % (0xff, 10, 105))
# 0xff 0xa 0xa
print("%#X %#X %#X" % (0xff, 10, 105))
# 0XFF 0XA 0XA
print("%#.0F %.0F" % (300, 300))
# 300. 300


print("'%d' — '%05d'" % (3, 3))  # 5 — ширина поля
# "'3' — '00003'"

print("'%5d' — '%-5d'" % (3, 3))  # 5 — ширина поля
# "'    3' — '3    '"
print("'%05d' — '%-05d'" % (3, 3))
# "'00003' — '3    '"


print("'% d' — '% d'" % (-3, 3))
# "'-3' — ' 3'"

print("'%+d' — '%+d'" % (-3, 3))
# "'-3' — '+3'"


print("'%10d' — '%-10d'" % (3, 3))
# "'         3' — '3         '"
print("'%3s''%10s'" % ("string", "string"))
# "'string''    string'"


print("'%*s''%10s'" % (10, "string", "str"))
# "'    string''       str'"


import math
print("%s %f %.2f" % (math.pi, math.pi, math.pi))
# '3.141592653589793 3.141593 3.14'


print("'%*.*f'" % (8, 5, math.pi))
# "' 3.14159'"


print("%s" % ("Обычная строка"))
# Обычная строка
print("%s %s %s" % (10, 10.52, [1, 2, 3]))
# 10 10.52 [1, 2, 3]


print("%r" % ("Обычная строка"))
# 'Обычная строка'


print("%a" % ("строка"))
# '\u0441\u0442\u0440\u043e\u043a\u0430'


for i in range(33, 127):
  print("%s => %c" % (i, i))


print("%d %d %d" % (10, 25.6, -80))
# 10 25 -80
print("%i %i %i" % (10, 25.6, -80))
# 10 25 -80


print("%o %o %o" % (0o77, 10, 105))
# 77 12 12
print("%#o %#o %#o" % (0o77, 10, 105))
# 0o77 0o12 0o12


print("%x %x %x" % (0xff, 10, 105))
# ff a a
print("%#x %#x %#x" % (0xff, 10, 105))
# 0xff 0xa 0xa


print("%X %X %X" % (0xff, 10, 105))
# FF A A
print("%#X %#X %#X" % (0xff, 10, 105))
# 0XFF 0XA 0XA


print("%f %f %f" % (300, 18.65781452, -12.5))
# 300.000000 18.657815 -12.500000
print("%F %F %F" % (300, 18.65781452, -12.5))
# 300.000000 18.657815 -12.500000
print("%#.0F %.0F" % (300, 300))
# 300. 300


print("%e %e" % (3000, 18657.81452))
# 3.000000e+03 1.865781e+04


print("%E %E" % (3000, 18657.81452))
# 3.000000E+03 1.865781E+04

print("%g %g %g" % (0.086578, 0.000086578, 1.865E-005))
# 0.086578 8.6578e-05 1.865e-05

print("%G %G %G" % (0.086578, 0.000086578, 1.865E-005))
# 0.086578 8.6578E-05 1.865E-05

# print("% %s" % ("- это символ процента")) # Ошибка
# Traceback (most recent call last):
#   File "<pyshell#55>", line 1, in <module>
#     print("% %s" % ("- это символ процента")) # Ошибка
# TypeError: not all arguments converted during string formatting
print("%% %s" % ("- это символ процента")) # Нормально
# % — это символ процента