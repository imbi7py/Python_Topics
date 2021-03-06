# # tarfile can also read and write TAR archives compressed using gzip, bzip2, and lzma compression.
# # To read or write to a compressed archive, use tarfile.open(), passing in the appropriate mode for
# # the compression type.
# #
# # For example, to read or write data to a TAR archive compressed using gzip, use the 'r:gz' or 'w:gz'
# # modes respectively:
#
# ______ t_f_
#
# files _ 'app.py', 'config.py', 'tests.py'
# w__ t_f_.o.. 'packages.tar.gz' m.._'_|__') __ ta_
#     ta_.a..'app.py'
#     ta_.a..'config.py'
#     ta_.a..'tests.py'
#
# w__ t_f_.o.. 'packages.tar.gz' m.._'_|__' __ t
#     ___ member __ ?.g_m..
#         print ?.n..
#
# # app.py
# # config.py
# # tests.py
# #
# # The 'w:gz' mode opens the archive for gzip compressed writing and 'r:gz' opens the archive
# # for gzip compressed reading. Opening compressed archives in append mode is not possible.
# # To add files to a compressed archive, you have to create a new archive.
