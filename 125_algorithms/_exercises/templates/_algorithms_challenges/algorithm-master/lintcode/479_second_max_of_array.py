class Solution:
    """
    @param: A: An integer array
    @return: The second max number in the array.
    """
    ___ secondMax(self, A
        __ not A:
            r_

        max1 = max2 = float('-inf')
        for a in A:
            __ a > max1:
                max2 = max1
                max1 = a
                continue
            __ a > max2:
                max2 = a

        r_ max2
