# Python makes retrieving file attributes such as file size and modified times easy. This is done through os.stat(),
# os.scandir(), or pathlib.Path(). os.scandir() and pathlib.Path() retrieve a directory listing with file attributes
# combined. This can be potentially more efficient than using os.listdir() to list files and then getting
# file attribute information for each file.
# The examples below show how to get the time the files in my_directory/ were last modified. The output is in seconds:
#
______ __
w__ __.scandir('my_directory/') __ dir_contents:
    ___ entry __ dir_contents:
        info = entry.stat()
        print(info.st_mtime)

print()
print()

# 1539032199.0052035
# 1539032469.6324475
# 1538998552.2402923
# 1540233322.4009316
# 1537192240.0497339
# 1540266380.3434134
#
# os.scandir() returns a ScandirIterator object. Each entry in a ScandirIterator object has a .stat()
# method that retrieves information about the file or directory it points to. .stat() provides information such as
# file size and the time of last modification. In the example above, the code prints out the st_mtime attribute,
# which is the time the content of the file was last modified.
#
# The pathlib module has corresponding methods for retrieving file information that give the same results:

from pathlib ______ Path
current_dir = Path('my_directory')
___ p.. __ current_dir.iterdir():
    info = p...stat()
    print(info.st_mtime)

print()
print()

# 1539032199.0052035
# 1539032469.6324475
# 1538998552.2402923
# 1540233322.4009316
# 1537192240.0497339
# 1540266380.3434134
#
# In the example above, the code loops through the object returned by .iterdir() and retrieves file attributes
# through a .stat() call for each file in the directory list. The st_mtime attribute returns a float value that
# represents seconds since the epoch. To convert the values returned by st_mtime for display purposes,
# you could write a helper function to convert the seconds into a datetime object:

from datetime ______ datetime
from __ ______ scandir

___ convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

___ get_files():
    dir_entries = scandir('my_directory/')
    ___ entry __ dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

# This will first get a list of files in my_directory and their attributes and then call convert_date()
# to convert each file’s last modified time into a human readable form. convert_date() makes use of .strftime()
# to convert the time in seconds into a string.
# The arguments passed to .strftime() are the following:
#
#     %d: the day of the month
#     %b: the month, in abbreviated form
#     %Y: the year
#
# Together, these directives produce output that looks like this:
#
get_files()

# file1.py        Last modified:  04 Oct 2018
# file3.txt       Last modified:  17 Sep 2018
# file2.txt       Last modified:  17 Sep 2018
#
# The syntax for converting dates and times into strings can be quite confusing. To read more about it,
# check out the official documentation on it. Another handy reference that is easy to remember is http://strftime.org/ .