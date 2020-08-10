# print('#' * 52)
# line _ 'aaa\nbbb\nccc\n'
# print ?.sp..'\n'
# # ['aaa', 'bbb', 'ccc', '']
# # ######################################################################################################################
#
# print('#' * 52 + 'splitlines')
# print(?.s_l..
# # ['aaa', 'bbb', 'ccc']
# # ######################################################################################################################
#
# print('#' * 52 + 'find')
# mystr _ 'xxxSPAMxxx'
# print ?.f.. 'SPAM' # return first offset
# # 3
# # ######################################################################################################################
#
# print('#' * 52 + 'replace')
# mystr _ 'xxaaxxaa'
# print(?.r..('aa', 'SPAM')) # global replacement
# # 'xxSPAMxxSPAM
# # ######################################################################################################################
#
# print('#' * 52 + 'in')
# mystr _ 'xxxSPAMxxx'
# print('SPAM' __ ?) # substring search/test
# # True
# # ######################################################################################################################
#
# print('Ni' __ ?) # when not found
# # False
# # ######################################################################################################################
#
# print(?.f.. 'Ni'
# # -1
# # ######################################################################################################################
# print('#' * 52 + 'strip')
# mystr _ '\t Ni\n'
# print(?.str..  # remove whitespace
# # 'Ni'
# # ######################################################################################################################
#
# print(?.rst..) # same, but just on right side
# # '\t Ni'
# # ######################################################################################################################
# print('#' * 52 + 'lower')
# mystr _ 'SHRUBBERY'
# print(?.l.. # case converters
# # 'shrubbery'
# # ######################################################################################################################
#
# print('#' * 52 + 'isalpha')
# print(?.isa.. # content tests
# # True
# # ######################################################################################################################
#
# print('#' * 52 + 'isdigit')
# print(?.isd..
# # False
# # ######################################################################################################################
#
# print('#' * 52 + 'ascii_lowercase')
# ______ string # case presets: for 'in', etc.
# print ?.a_l..
# # 'abcdefghijklmnopqrstuvwxyz'
# # ######################################################################################################################
#
# print(?.w.. # whitespace characters
# # ' \t\n\r\x0b\x0c'
# # ######################################################################################################################
#
# print('#' * 52 + ' split into substrings list')
# mystr _ 'aaa,bbb,ccc'
# print(?.sp.. ',' # split into substrings list
# # ['aaa', 'bbb', 'ccc']
# # ######################################################################################################################
#
# print('#' * 52 + 'default delimiter: whitespace')
# mystr _ 'a b\nc\nd'
# print(?.sp.. # default delimiter: whitespace
# # ['a', 'b', 'c', 'd']
# # ######################################################################################################################
#
# print('#' * 52 + 'join substrings list')
# delim _ 'NI'
# print(?.j.. 'aaa', 'bbb', 'ccc' # join substrings list
# # 'aaaNIbbbNIccc'
# # ######################################################################################################################
#
# print('#' * 52 + 'add a space between')
# print(' '.j..(['A', 'dead', 'parrot'])) # add a space between
# # 'A dead parrot
# # ######################################################################################################################
#
# print('#' * 52 + 'convert to characters list')
# chars _ li.. ('Lorreta') # convert to characters list
# print ?
# # ['L', 'o', 'r', 'r', 'e', 't', 'a']
# # ######################################################################################################################
#
# print('#' * 52 + 'to string: empty delimiter')
# print(?.ap.. '!'
# print(''.j.. ? # to string: empty delimiter
# # 'Lorreta!'
# # ######################################################################################################################
#
# print('#' * 52 + 'str.replace, the hard way!e')
# mystr _ 'xxaaxxaa'
# print('SPAM'.j.. ?.sp.. 'aa'   # str.replace, the hard way!
# # 'xxSPAMxxSPAM'
# # ######################################################################################################################
#
# # (42, 42)
# print('#' * 52 + 'int to string conversions')
# print(st. 42 re.. 42 # int to string conversions
# # ('42', '42')
# # ######################################################################################################################
#
# print('#' * 52 + 'via formatting expression, method')
# print(("@" % 42), '|__'.f.. 42 # via formatting expression, method
# # ('42', '42')
# # ######################################################################################################################
#
# print('#' * 52 + 'concatenation, addition')
# print("42" + st. 1 in. "42") + 1) # concatenation, addition
# # ('421', 43)
# # ######################################################################################################################