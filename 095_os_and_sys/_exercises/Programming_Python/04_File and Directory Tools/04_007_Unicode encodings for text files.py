data = 'sp\xe4m'
data
#'späm'
0xe4, bin(0xe4), chr(0xe4)
# (228, '0b11100100', 'ä')

data.encode('latin1') # 8-bit characters: ascii + extras
# b'sp\xe4m'
data.encode('utf8') # 2 bytes for special characters only
# b'sp\xc3\xa4m'
data.encode('ascii') # does not encode per ascii
# UnicodeEncodeError: 'ascii' codec can't encode character '\xe4' in position 2:
ordinal not in range(128)

data.encode('utf16') # 2 bytes per character plus preamble
# b'\xff\xfes\x00p\x00\xe4\x00m\x00'
data.encode('cp500') # an ebcdic encoding: very different
# b'\xa2\x97C\x94'

open('data.txt', 'w', encoding='latin1').write(data)
# 4
open('data.txt', 'r', encoding='latin1').read()
# 'späm'
open('data.txt', 'rb').read()
# b'sp\xe4m'

open('data.txt', 'w', encoding='utf8').write(data) # encode data per utf8
# 4
open('data.txt', 'r', encoding='utf8').read() # decode: undo encoding
# 'späm'
open('data.txt', 'rb').read() # no data translations
# b'sp\xc3\xa4m'

open('data.txt', 'w', encoding='ascii').write(data)
# UnicodeEncodeError: 'ascii' codec can't encode character '\xe4' in position 2:
ordinal not in range(128)
open(r'C:\Python31\python.exe', 'r').read()
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2:
#character maps to <undefined>

>>> open('data.txt', 'w', encoding='cp500').writelines(['spam\n', 'ham\n'])
>>> open('data.txt', 'r', encoding='cp500').readlines()
['spam\n', 'ham\n']
>>> open('data.txt', 'r').readlines()
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 2:
character maps to <undefined>
>>> open('data.txt', 'rb').readlines()
[b'\xa2\x97\x81\x94\r%\x88\x81\x94\r%']

>>> open('data.txt', 'rb').read()
b'\xa2\x97\x81\x94\r%\x88\x81\x94\r%'