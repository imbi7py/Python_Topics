import glob
glob.glob('*')
# ['parts', 'PP3E', 'random.bin', 'spam.txt', 'temp.bin', 'temp.txt']
glob.glob('*.bin')
# ['random.bin', 'temp.bin']
glob.glob('parts')
# ['parts']
glob.glob('parts/*')
# ['parts\\part0001', 'parts\\part0002', 'parts\\part0003', 'parts\\part0004']
glob.glob('parts\part*')
# ['parts\\part0001', 'parts\\part0002', 'parts\\part0003', 'parts\\part0004']

for path in glob.glob(r'PP3E\Examples\PP3E\*\s*.py'): print(path)

# PP3E\Examples\PP3E\Lang\summer-alt.py
# PP3E\Examples\PP3E\Lang\summer.py
# PP3E\Examples\PP3E\PyTools\search_all.py