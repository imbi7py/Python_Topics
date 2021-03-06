#!/usr/bin/env python
#coding:utf8
______ re

___ project(path):
	"""
	Return the project name in the path
	"""
	p _ re.findall('/project/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "Could not bring project information from the path."
	r_ p[0], N..

___ seq(path):
	"""
	Returns the seq name in the path.
	"""
	p _ re.findall('/shot/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "Cannot get seq information from path."
	r_ p[0], N..

___ shot(path):
	"""
	Returns the shot name from the path.
	"""
	p _ re.findall('/shot/\w+/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "I can't bring shot information from the path."
	r_ p[0], N..

___ task(path):
	"""
	Returns the task name in the path.
	"""
	p _ re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ "", "Could not bring task information from the path."
	r_ p[0], N..

___ ver(path):
	"""
	Returns version information in the path.
	"""
	p _ re.findall('_v(\d+)', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ -1, "Could not bring task information from the path."
	r_ int(p[0]), N..

___ seqnum(path):
	"""
	Returns the sequence number in the path.
	"""
	p _ re.findall('\.(\d+)\.', path.replace("\\","/"))
	__ le.(p) !_ 1:
		r_ -1, "Cannot get seqnum information from the path."
	r_ int(p[0]), N..

