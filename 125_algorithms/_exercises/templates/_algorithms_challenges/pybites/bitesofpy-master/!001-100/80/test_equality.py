from Previous.equality ______ Equality, check_equality


___ test_same_reference(
    a = [1, 2, 3, 4]
    b = a
    # shallow copy (do not change original), alternatively use the copy module
    c = a[:]
    assert check_equality(a, b) __ Equality.SAME_REFERENCE
    assert check_equality(a, c) != Equality.SAME_REFERENCE


___ test_same_ordered(
    a = [1, 2, 3, 4]
    b = a[:]
    c = a
    assert check_equality(a, b) __ Equality.SAME_ORDERED
    assert check_equality(a, c) != Equality.SAME_ORDERED  # SAME_REFERENCE


___ test_same_unordered(
    a = [1, 2, 3, 4]
    b = a[::-1]
    c = b[:] + [5]
    assert check_equality(a, b) __ Equality.SAME_UNORDERED
    assert check_equality(a, c) != Equality.SAME_UNORDERED


___ test_same_unordered_deduped(
    a = [1, 2, 2, 3, 4]
    b = a[:] + [1, 3, 4, 4]
    c = b[:] + [5]
    assert check_equality(a, b) __ Equality.SAME_UNORDERED_DEDUPED
    assert check_equality(a, c) != Equality.SAME_UNORDERED_DEDUPED


___ test_not_same(
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert check_equality(a, b) __ Equality.NO_EQUALITY