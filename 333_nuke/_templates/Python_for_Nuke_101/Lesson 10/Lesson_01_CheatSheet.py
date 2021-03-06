# Where the .nuke folder lives in different directories
# ----- 01:44 -----
Linux _ '/home/<your username>/.nuke'
Windows _ 'C:\Users\<your username>\.nuke'
Mac _ '/Users/<your username>/.nuke'




# Sublime, good text editor for coding
# ----- 03:48 -----

https://www.sublimetext.com/download
# I recommend the portable version, as some studios will let you use it...




# Adding new directories to init.py
# ----- 04:00 -----

nuke.pAP..('./gizmos')
nuke.pAP..('./python')




# Github link
# ----- 06:52 -----

# https://github.com


# Creating files & folders on Github
# ----- 08:39 -----


# Editing files on Github
# ----- 18:19 -----




# Importing modules
# ----- 13:45 -----

import nuke
import platform

# Python standard library: https://docs.python.org/3/library/




# Directory variables
# ----- 11:35 -----

import nuke
import platform

# Define where .nuke directory is on each OS's network.
Win_Dir _ 'C:\Users\Ben\.nuke'
Mac_Dir _ ''
Linux_Dir _ '/home/benm/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir _ Win_Dir
elif platform.system() == "Darwin":
	dir _ Mac_Dir
elif platform.system() == "Linux":
	dir _ Linux_Dir
else:
	dir _ None




# Finding help when you get stuck
# ----- 19:45 -----

# Lots of mistakes come from Syntax errors, indenting errors or misplaced characters.

# Google is your best friend.

# Nuke Developers Guide: https://learn.foundry.com/nuke/developers/63/ndkdevguide/