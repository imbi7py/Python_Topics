# # Python provides a handy module for creating temporary files and directories called tempfile.
# # tempfile can be used to open and store data temporarily in a file or directory while your program is running.
# # tempfile handles the deletion of the temporary files when your program is done with them.
# #
# # Here’s how to create a temporary file:
# #
# ______ __
# ____ tempfile ______ TF..
#
# # Create a temporary file and write some data to it
# fp _ TF.. '___'
# ?.w..('Hello universe!')
#
# # Go back to the beginning and read data from file
# ?.s.. 0
# data _ ?.r..
#
# # Close the file, after which it will be removed
# ?.cl..
#
# # The first step is to ______ TemporaryFile from the tempfile module. Next, create a file like object using
# # the TemporaryFile() method by calling it and passing the mode you want to open the file in. This will create and open
# # a file that can be used as a temporary storage area. In the example above, the mode is 'w+t', which makes tempfile
# # create a temporary text file in write mode. There is no need to give the temporary file a filename since
# # it will be destroyed after the script is done running. After writing to the file, you can read from it and close
# # it when you’re done processing it. Once the file is closed, it will be deleted from the filesystem. If you need
# # to name the temporary files produced using tempfile, use tempfile.NamedTemporaryFile(). The temporary files and
# # directories created using tempfile are stored in a special system directory for storing temporary files.
# # Python searches a standard list of directories to find one that the user can create files in.
# # On Windows, the directories are C:\TEMP, C:\TMP, \TEMP, and \TMP, in that order. On all other platforms,
# # the directories are /tmp, /var/tmp, and /usr/tmp, in that order. As a last resort, tempfile will save temporary files
# # and directories in the current directory. .TemporaryFile() is also a context manager so it can be used in conjunction
# # with the with statement. Using a context manager takes care of closing and deleting the file automatically after it
# # has been read:
#
# w__ TemporaryFile ___ __ fp
#     ?.w.. 'Hello universe!'
#     ?.s.. 0
#     ?.r..
# # File is now closed and removed
#
# # This creates a temporary file and reads data from it. As soon as the file’s contents are read, the temporary file is
# # closed and deleted from the file system.
# # tempfile can also be used to create temporary directories. Let’s look at how you can do this using tempfile.TemporaryDirectory():
#
# ______ tempfile
# w__ ?.TD.. __ tmpdir
#     print('Created temporary directory ' ?
#     __.p...e.. ?
#
#
# # Created temporary directory  /tmp/tmpoxbkrm6c
# # True
# #
# # >>> # Directory contents have been removed
# # ...
# # >>> tmpdir
# # '/tmp/tmpoxbkrm6c'
# # >>> os.path.exists(tmpdir)
# # False
# #
# # Calling tempfile.TemporaryDirectory() creates a temporary directory in the file system and returns an object
# # representing this directory. In the example above, the directory is created using a context manager, and the name
# # of the directory is stored in tmpdir. The third line prints out the name of the temporary directory,
# # and os.path.exists(tmpdir) confirms if the directory was actually created in the file system.
# # After the context manager goes out of context, the temporary directory is deleted and a call to os.path.exists(tmpdir)
# # returns False, which means that the directory was succesfully deleted.