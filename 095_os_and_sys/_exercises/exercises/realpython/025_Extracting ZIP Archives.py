# # The zipfile module allows you to extract one or more files from ZIP archives through .extract() and .extractall().
# #
# # These methods extract files to the current directory by default. They both take an optional path parameter
# # that allows you to specify a different directory to extract files to. If the directory does not exist,
# # it is automatically created. To extract files from the archive, do the following:
#
# ______ z_f_
# ______ __
#
# __.l_d_('.')
#
# # ['data.zip']
#
# data_zip _ z_f_.ZF.. 'data.zip' _
#
# # Extract a single file to current directory
# ?.e... 'file1.py'
#
# # '/home/terra/test/dir1/zip_extract/file1.py'
#
# __.l_d_ '.'
#
# # ['file1.py', 'data.zip']
#
# # Extract all files into a different directory
# ?.e_a.. p.._'extract_dir/'
#
# __.l_d_ '.'
# # ['file1.py', 'extract_dir', 'data.zip']
#
# __.l_d_ 'extract_dir'
# # ['file1.py', 'file3.py', 'file2.py', 'sub_dir']
#
# ?.cl..
#
# # The third line of code is a call to os.listdir(), which shows that the current directory has only one file, data.zip.
# #
# # Next, you open data.zip in read mode and call .extract() to extract file1.py from it. .extract() returns
# # the full file path of the extracted file. Since there’s no path specified, .extract() extracts file1.py
# # to the current directory.
# #
# # The next line prints a directory listing showing that the current directory now includes the extracted file
# # in addition to the original archive. The line after that shows how to extract the entire archive into
# # the zip_extract directory. .extractall() creates the extract_dir and extracts the contents of data.zip into it.
# # The last line closes the ZIP archive.
