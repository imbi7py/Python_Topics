print('#' * 52)
line = 'aaa\nbbb\nccc\n'
print(line.split('\n'))
# ['aaa', 'bbb', 'ccc', '']

print('#' * 52 + 'splitlines')
print(line.splitlines())
# ['aaa', 'bbb', 'ccc']

print('#' * 52 + 'find')
mystr = 'xxxSPAMxxx'
print(mystr.find('SPAM')) # return first offset
# 3
print('#' * 52 + 'replace')
mystr = 'xxaaxxaa'
print(mystr.replace('aa', 'SPAM')) # global replacement
# 'xxSPAMxxSPAM

print('#' * 52 + 'in')
mystr = 'xxxSPAMxxx'
print('SPAM' in mystr) # substring search/test
# True
print('Ni' in mystr) # when not found
# False
print(mystr.find('Ni'))
# -1
print('#' * 52 + 'strip')
mystr = '\t Ni\n'
print(mystr.strip())  # remove whitespace
# 'Ni'
print(mystr.rstrip()) # same, but just on right side
# '\t Ni'

print('#' * 52 + 'lower')
mystr = 'SHRUBBERY'
print(mystr.lower()) # case converters
# 'shrubbery'

print('#' * 52 + 'isalpha')
print(mystr.isalpha()) # content tests
# True

print('#' * 52 + 'isdigit')
print(mystr.isdigit())
# False

print('#' * 52 + 'ascii_lowercase')
import string # case presets: for 'in', etc.
print(string.ascii_lowercase)
# 'abcdefghijklmnopqrstuvwxyz'
print(string.whitespace) # whitespace characters
# ' \t\n\r\x0b\x0c'

print('#' * 52 + ' split into substrings list')
mystr = 'aaa,bbb,ccc'
print(mystr.split(',')) # split into substrings list
# ['aaa', 'bbb', 'ccc']

print('#' * 52 + 'default delimiter: whitespace')
mystr = 'a b\nc\nd'
print(mystr.split()) # default delimiter: whitespace
# ['a', 'b', 'c', 'd']

print('#' * 52 + 'join substrings list')
delim = 'NI'
print(delim.join(['aaa', 'bbb', 'ccc'])) # join substrings list
# 'aaaNIbbbNIccc'

print('#' * 52 + 'add a space between')
print(' '.join(['A', 'dead', 'parrot'])) # add a space between
# 'A dead parrot

print('#' * 52 + 'convert to characters list')
chars = list('Lorreta') # convert to characters list
print(chars)
# ['L', 'o', 'r', 'r', 'e', 't', 'a']

print('#' * 52 + 'to string: empty delimiter')
print(chars.append('!'))
print(''.join(chars)) # to string: empty delimiter
# 'Lorreta!'

print('#' * 52 + 'str.replace, the hard way!e')
mystr = 'xxaaxxaa'
print('SPAM'.join(mystr.split('aa'))) # str.replace, the hard way!
# 'xxSPAMxxSPAM'

# (42, 42)
print('#' * 52 + 'int to string conversions')
print(str(42), repr(42)) # int to string conversions
# ('42', '42')

print('#' * 52 + 'via formatting expression, method')
print(("%d" % 42), '{:d}'.format(42)) # via formatting expression, method
# ('42', '42')

print('#' * 52 + 'concatenation, addition')
print("42" + str(1), int("42") + 1) # concatenation, addition
# ('421', 43)