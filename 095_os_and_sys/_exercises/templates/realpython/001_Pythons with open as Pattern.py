# # Reading and writing data to files using Python is pretty straightforward. To do this, you must first open files in
# # the appropriate mode. Here’s an example of how to use Python’s “with open(…) as …” pattern to open a text file
# # and read its contents:
# #
# w__ o.. data.txt _ __ f
#     data _ ?.r..
# #
# # open() takes a filename and a mode as its arguments. r opens the file in read only mode. To write data to a file,
# # pass in w as an argument instead:
# #
# w__ o.. data.txt _ __ f
#     data _ 'some data to be written to the file'
#     ?.w.. ?
# #
# # In the examples above, open() opens files for reading or writing and returns a file handle (f in this case)
# # that provides methods that can be used to read or write data to the file. Read Working With File I/O in Python
# # for more information on how to read and write to files.