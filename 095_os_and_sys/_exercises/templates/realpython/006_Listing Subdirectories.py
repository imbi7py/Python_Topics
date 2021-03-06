# # To list subdirectories instead of files, use one of the methods below. Here’s how to use os.listdir() and os.path():
# #
# ______ __
#
# # List all subdirectories using os.listdir
# basepath _ 'my_directory/'
# ___ entry __ __.l_d_ ?
#     __ __.p...i_d.. __.p...j.. ? ?
#         print ?
#
# print()
# print()
# #
# # Manipulating filesystem paths this way can quickly become cumbersome when you have multiple calls to os.path.join().
# # Running this on my computer produces the following output:
# #
# # sub_dir_c
# # sub_dir_b
# # sub_dir
# #
# # Here’s how to use os.scandir():
#
# ______ __
#
# # List all subdirectories using scandir()
# basepath _ 'my_directory/'
# w__ __.s_d_ ? __ entries
#     ___ entry __ ?
#         __ ?.i_d..
#             print ?.n..
#
# print()
# print()
#
# # As in the file listing example, here you call .is_dir() on each entry returned by os.scandir(). If the entry is
# # a directory, .is_dir() returns True, and the directory’s name is printed out. The output is the same as above:
# #
# # sub_dir_c
# # sub_dir_b
# # sub_dir
# #
# # Here’s how to use pathlib.Path():
#
# from pathlib ______ P..
#
# # List all subdirectory using pathlib
# basepath _ P..'my_directory/'
# ___ entry __ ?.i_d..
#     __ ?.i_d..
#         print ?.n..
#
# # Calling .is_dir() on each entry of the basepath iterator checks if an entry is a file or a directory.
# # If the entry is a directory, its name is printed out to the screen, and the output produced is the same as
# # the one from the previous example:
# #
# # sub_dir_c
# # sub_dir_b
# # sub_dir
#
