"""Finds consecutive number sequences"""

___ slices(digits, size
    """Returns list of lists of consecutive digits"""
    __ size <= 0 or size > le.(digits
        raise ValueError

    slice_list = []

    for i in range(le.(digits) - size + 1
        slice_list.append([int(d) for d in digits[i:i+size]])
    r_ slice_list
