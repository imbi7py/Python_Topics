import os

print(os.getpid())
# 7980
print(os.getcwd())
# 'C:\\PP4thEd\\Examples\\PP4E\\System'
os.chdir(r'C:\Users')
print(os.getcwd())
# 'C:\\Users'