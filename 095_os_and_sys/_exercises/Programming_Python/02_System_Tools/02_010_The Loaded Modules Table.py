import sys
print(sys.modules)
# {'reprlib': <module 'reprlib' from 'c:\python31\lib\reprlib.py'>, ...more deleted...
list(sys.modules.keys())
# ['reprlib', 'heapq', '__future__', 'sre_compile', '_collections', 'locale', '_sre',
# 'functools', 'encodings', 'site', 'operator', 'io', '__main__', ...more deleted... ]
print(sys)
# <module 'sys' (built-in)>
print(sys.modules['sys'])
# <module 'sys' (built-in)>
