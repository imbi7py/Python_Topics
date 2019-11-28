import os
os.listdir('.')
# ['parts', 'PP3E', 'random.bin', 'spam.txt', 'temp.bin', 'temp.txt']

os.listdir(os.curdir)
# ['parts', 'PP3E', 'random.bin', 'spam.txt', 'temp.bin', 'temp.txt']

os.listdir('parts')
# ['part0001', 'part0002', 'part0003', 'part0004']

os.popen('dir /b parts').readlines()
# ['part0001\n', 'part0002\n', 'part0003\n', 'part0004\n']

glob.glob(r'parts\*')
# ['parts\\part0001', 'parts\\part0002', 'parts\\part0003', 'parts\\part0004']

os.listdir('parts')
# ['part0001', 'part0002', 'part0003', 'part0004']

