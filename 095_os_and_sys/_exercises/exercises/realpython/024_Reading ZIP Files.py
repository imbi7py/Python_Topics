# # The zipfile module is a low level module that is part of the Python Standard Library. zipfile has functions that make
# # it easy to open and extract ZIP files. To read the contents of a ZIP file, the first thing to do is to create
# # a ZipFile object. ZipFile objects are similar to file objects created using open(). ZipFile is also
# # a context manager and therefore supports the with statement:
#
# # ______ zipfile
# #
# # with zipfile.ZipFile('data.zip', 'r') as zipobj:
#
#
# # Here, you create a ZipFile object, passing in the name of the ZIP file to open in read mode. After opening
# # a ZIP file, information about the archive can be accessed through functions provided by the zipfile module.
# # The data.zip archive in the example above was created from a directory named data that contains a total
# # of 5 files and 1 subdirectory:
# #
# # .
# # |
# # ├── sub_dir/
# # |   ├── bar.py
# # |   └── foo.py
# # |
# # ├── file1.py
# # ├── file2.py
# # └── file3.py
# #
# # To get a list of files in the archive, call namelist() on the ZipFile object:
#
# ______ z_f_
#
# w__ z_f_.ZF.. 'data.zip' _ __ zipobj:
#     ?.n_l..
#
# # This produces a list:
# #
# # ['file1.py', 'file2.py', 'file3.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
# #
# # .namelist() returns a list of names of the files and directories in the archive. To retrieve information about
# # the files in the archive, use .getinfo():
#
# ______ z_f_
#
# w__ z_f_.ZF.. 'data.zip' _ __ zipobj
#     bar_info _ ?.g_i.. 'sub_dir/bar.py'
#     ?.f_s..
#
# # Here’s the output:
# #
# # 15277
# #
# # .getinfo() returns a ZipInfo object that stores information about a single member of the archive. To get information
# # about a file in the archive, you pass its path as an argument to .getinfo(). Using getinfo(), you’re able
# # to retrieve information about archive members such as the date the files were last modified, their compressed sizes,
# # and their full filenames. Accessing .file_size retrieves the file’s original size in bytes.
# #
# # The following example shows how to retrieve more details about archived files in a Python REPL.
# # Assume that the zipfile module has been imported and bar_info is the same object you created in previous examples:
#
# ?.d_t..
# # (2018, 10, 7, 23, 30, 10)
# ?.c_s..
# # 2856
# ?.f_n..
# # 'sub_dir/bar.py'
#
# # bar_info contains details about bar.py such as its size when compressed and its full path.
# #
# # The first line shows how to retrieve a file’s last modified date. The next line shows how to get the size of
# # the file after compression. The last line shows the full path of bar.py in the archive.
# # ZipFile supports the context manager protocol, which is why you’re able to use it with the with statement.
# # Doing this automatically closes the ZipFile object after you’re done with it. Trying to open or extract files from
# # a closed ZipFile object will result in an error.