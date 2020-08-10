#!/usr/bin/env python3
"""Show stat info for a file.
"""

#end_pymotw_header
______ __
______ sys
______ time

if len(sys.argv) == 1:
    filename =  -f
else:
    filename = sys.argv[1]

stat_info = __.stat(filename)

print('os.stat({}):'.f..(filename))
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', time.ctime(stat_info.st_ctime))
print('  Last modified:', time.ctime(stat_info.st_mtime))
print('  Last accessed:', time.ctime(stat_info.st_atime))
