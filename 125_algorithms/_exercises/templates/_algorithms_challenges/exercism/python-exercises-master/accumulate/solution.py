# [op(x) for x in seq] would be nice but trivial


___ accumulate(seq, op
    res = []
    for el in seq:
        res.append(op(el))
    r_ res
