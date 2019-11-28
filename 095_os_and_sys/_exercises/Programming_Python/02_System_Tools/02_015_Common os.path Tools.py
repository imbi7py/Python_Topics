import sys, os

print('#' * 52 + 'isfile')
print(os.path.isdir(r'C:\Users')), print(os.path.isfile(r'C:\Users'))
# (True, False)
print(os.path.isdir(r'C:\config.sys')), print(os.path.isfile(r'C:\config.sys'))
# (False, True)
print(os.path.isdir('nonesuch')), print(os.path.isfile('nonesuch'))
print(os.path.isdir(r'C:\Users\Sergej\Downloads'))
#(False, False)
#
print('#' * 52 + 'exists')
print(os.path.exists(r'c:\Users\Brian'))
# False
print(os.path.exists(r'c:\Users\Default'))
# True

print('#' * 52 + 'getsize')
print(os.path.getsize(r'C:\bdlog.txt'))
# 24
#
print('#' * 52 + 'join')
# ('C:\\temp', 'data.txt')
print(os.path.join(r'C:\temp', 'output.txt'))
# 'C:\\temp\\output.txt'

print('#' * 52 + 'basename')
name = r'C:\temp\data.txt' # Windows paths
print(os.path.dirname(name)), print(os.path.basename(name))
# ('C:\\temp', 'data.txt')
name = '/home/lutz/temp/data.txt' # Unix-style paths
print(os.path.dirname(name)), print(os.path.basename(name))
# ('/home/lutz/temp', 'data.txt')

print('#' * 52 + 'splitext')
print(os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'))
# ('C:\\PP4thEd\\Examples\\PP4E\\PyDemos', '.pyw')

print('#' * 52 + 'pathname - split')
print(os.sep)
# '\\'
pathname = r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'
print(os.path.split(pathname)) # split file from dir
# ('C:\\PP4thEd\\Examples\\PP4E', 'PyDemos.pyw')
print(pathname.split(os.sep)) # split on every slash
# ['C:', 'PP4thEd', 'Examples', 'PP4E', 'PyDemos.pyw']
print(os.sep.join(pathname.split(os.sep)))
# 'C:\\PP4thEd\\Examples\\PP4E\\PyDemos.pyw'
print(os.path.join(*pathname.split(os.sep)))
# 'C:PP4thEd\\Examples\\PP4E\\PyDemos.pyw'

print('#' * 52 + 'normpath')
mixed = 'C:\\temp\\public/files/index.html'
print(os.path.normpath(mixed))
# 'C:\\temp\\public\\files\\index.html'
print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))
# C:\temp\sub\file.ext

print('#' * 52 + 'abspath')
os.chdir(r'C:\Users')
print(os.getcwd())
# 'C:\\Users'
print(os.path.abspath('')) # empty string means the cwd
# 'C:\\Users'
print(os.path.abspath('temp')) # expand to full pathname in cwd
# 'C:\\Users\\temp'
print(os.path.abspath(r'PP4E\dev')) # partial paths relative to cwd
# 'C:\\Users\\PP4E\\dev'
print(os.path.abspath('.')) # relative path syntax expanded
# 'C:\\Users'
print(os.path.abspath('..'))
# 'C:\\'
print(os.path.abspath(r'..\examples'))
# 'C:\\examples'
print(os.path.abspath(r'C:\PP4thEd\chapters')) # absolute paths unchanged
# 'C:\\PP4thEd\\chapters'
print(os.path.abspath(r'C:\temp\spam.txt'))
# 'C:\\temp\\spam.txt'