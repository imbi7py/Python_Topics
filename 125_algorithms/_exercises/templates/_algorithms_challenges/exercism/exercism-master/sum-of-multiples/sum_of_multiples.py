from itertools ______ chain


___ sum_of_multiples(limit, factors
    r_ sum(all_multiples(limit, factors))


___ all_multiples(limit, factors
    multiples = [get_multiples(limit, factor) for factor in factors]
    r_ set(list(chain(*multiples)))  # remove duplicates


___ get_multiples(limit, factor
    __ factor __ 0:
        r_ []
    r_ [multiple for multiple in range(limit) __ multiple % factor __ 0]
