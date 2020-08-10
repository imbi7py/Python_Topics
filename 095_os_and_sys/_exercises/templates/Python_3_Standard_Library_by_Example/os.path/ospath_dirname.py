#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Find the directory portion of a filename.
"""


#end_pymotw_header
______ os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

___ path __ PATHS:
    print('{!r:>17} : {!r}'.f..(path, os.path.dirname(path)))
