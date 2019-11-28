from io import StringIO
buff = StringIO() # save written text to a string
print(buff.write('spam\n'))
# 5
print(buff.write('eggs\n'))
# 5
print(buff.getvalue())
# 'spam\neggs\n'
buff = StringIO('ham\nspam\n') # provide input from a string
print(buff.readline())
# 'ham\n'
print(buff.readline())
# 'spam\n'
print(buff.readline())
# ''

print('#' * 52)
from io import StringIO
import sys
buff = StringIO()
temp = sys.stdout
sys.stdout = buff
print(42, 'spam', 3.141) # or print(..., file=buff)
#
sys.stdout = temp # restore original stream
print(buff.getvalue())
# '42 spam 3.141\n'

from io import BytesIO
stream = BytesIO()
stream.write(b'spam')
print(stream.getvalue())
# b'spam'
stream = BytesIO(b'dpam')
print(stream.read())
# b'dpam'