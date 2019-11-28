open('temp.txt', 'w').write('shrubbery\n') # text output mode: \n -> \r\n
# 10
open('temp.txt', 'rb').read() # binary input: actual file bytes
# b'shrubbery\r\n'
open('temp.txt', 'r').read() # test input mode: \r\n -> \n
# 'shrubbery\n'

data = b'a\0b\rc\r\nd' # 4 escape code bytes, 4 normal
len(data)
# 8
open('temp.bin', 'wb').write(data) # write binary data to file as is
# 8
open('temp.bin', 'rb').read() # read as binary: no translation
# b'a\x00b\rc\r\nd'

open('temp.bin', 'r').read() # text mode read: botches \r !
# 'a\x00b\nc\nd'

open('temp.bin', 'w').write(data) # must pass str for text mode
# TypeError: must be str, not bytes # use bytes.decode() for to-str
data.decode()
# 'a\x00b\rc\r\nd'

open('temp.bin', 'w').write(data.decode())
# 8
open('temp.bin', 'rb').read() # text mode write: added \r !
# b'a\x00b\rc\r\r\nd'
open('temp.bin', 'r').read() # again drops, alters \r on input
# 'a\x00b\nc\n\nd'