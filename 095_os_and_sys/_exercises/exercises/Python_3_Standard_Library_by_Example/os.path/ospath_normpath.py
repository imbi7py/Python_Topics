#!/usr/bin/env python3
# encoding: utf-8
#
#
"""Compute a "normalized" path.
"""


#end_pymotw_header
import os.path

PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three']


for path in PATHS:
    print('{!r:>22} : {!r:}'.format(path, os.path.normpath(path)))
