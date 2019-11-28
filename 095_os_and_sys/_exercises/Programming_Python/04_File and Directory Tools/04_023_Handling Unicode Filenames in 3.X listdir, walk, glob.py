# C:\...\PP4E\System\Filetools> python
import os
os.listdir('.')[:4]
# ['bigext-tree.py', 'bigpy-dir.py', 'bigpy-path.py', 'bigpy-tree.py']
os.listdir(b'.')[:4]
# [b'bigext-tree.py', b'bigpy-dir.py', b'bigpy-path.py', b'bigpy-tree.py']

for (dir, subs, files) in os.walk('..'): print(dir)

# ..
# ..\Environment
# ..\Filetools
# ..\Processes
for (dir, subs, files) in os.walk(b'..'): print(dir)

# b'..'
# b'..\\Environment'
# b'..\\Filetools'
# b'..\\Processes'

glob.glob('.\*')[:3]
# ['.\\bigext-out.txt', '.\\bigext-tree.py', '.\\bigpy-dir.py']

glob.glob(b'.\*')[:3]
# [b'.\\bigext-out.txt', b'.\\bigext-tree.py', b'.\\bigpy-dir.py']

name = '.'
os.listdir(name.encode())[:4]
# [b'bigext-out.txt', b'bigext-tree.py', b'bigpy-dir.py', b'bigpy-path.py']