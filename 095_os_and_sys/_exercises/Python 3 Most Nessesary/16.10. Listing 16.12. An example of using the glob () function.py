import os, glob
os.listdir("C:\\book\\folder1\\")
# ['file.txt', 'file1.txt', 'file2.txt', 'folder1_1', 'folder1_2',
# 'index.html']
glob.glob("C:\\book\\folder1\\*.txt")
# ['C:\\book\\folder1\\file.txt', 'C:\\book\\folder1\\file1.txt',
# 'C:\\book\\folder1\\file2.txt']
glob.glob("C:\\book\\folder1\\*.html") # Абсолютный путь
# ['C:\\book\\folder1\\index.html']
glob.glob("folder1/*.html")            # Относительный путь
# ['folder1\\index.html']
glob.glob("C:\\book\\folder1\\*[0-9].txt")
# ['C:\\book\\folder1\\file1.txt', 'C:\\book\\folder1\\file2.txt']
glob.glob("C:\\book\\folder1\\*\\*.html")
# ['C:\\book\\folder1\\folder1_1\\index.html',
# 'C:\\book\\folder1\\folder1_2\\test.html']
