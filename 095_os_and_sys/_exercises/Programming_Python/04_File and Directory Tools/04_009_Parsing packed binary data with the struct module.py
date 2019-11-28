import struct
data = struct.pack('>i4shf', 2, 'spam', 3, 1.234)
data
# b'\x00\x00\x00\x02spam\x00\x03?\x9d\xf3\xb6'
file = open('data.bin', 'wb')
file.write(data)
# 14
file.close()

import struct
file = open('data.bin', 'rb')
bytes = file.read()
values = struct.unpack('>i4shf', data)
values
# (2, b'spam', 3, 1.2339999675750732)

bin(values[0] | 0b1) # accessing bits and bytes
# '0b11'
values[1], list(values[1]), values[1][0]
# (b'spam', [115, 112, 97, 109], 115)

bytes
# b'\x00\x00\x00\x02spam\x00\x03?\x9d\xf3\xb6'
bytes[4:8]
# b'spam'

number = bytes[8:10]
number
# b'\x00\x03'
struct.unpack('>h', number)
# (3,)