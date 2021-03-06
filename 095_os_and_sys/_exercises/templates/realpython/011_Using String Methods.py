# # Python has several built-in methods for modifying and manipulating strings. Two of these methods, .startswith()
# # and .endswith(), are useful when you’re searching for patterns in filenames. To do this, first get a directory listing
# # and then iterate over it:
#
# ______ __
#
# # Get .txt files
# ___ f_name __ __.l_d_ 'some_directory'
#     __ f_name.e_w_ '.txt'
#         print ?
#
# # The code above finds all the files in some_directory/, iterates over them and uses .endswith() to print out
# # the filenames that have the .txt file extension. Running this on my computer produces the following output:
# #
# # data_01.txt
# # data_03.txt
# # data_03_backup.txt
# # data_02_backup.txt
# # data_02.txt
# # data_01_backup.txt
#
