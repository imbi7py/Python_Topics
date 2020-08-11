#!/usr/bin/env python3
# encoding: utf-8
#
#
"""Determine the base filename from a path.
"""


#end_pymotw_header
import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.'
    '']


for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))
