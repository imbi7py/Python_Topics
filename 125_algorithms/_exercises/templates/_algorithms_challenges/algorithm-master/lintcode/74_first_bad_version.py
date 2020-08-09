"""
Main Concept
    ver. | 1 2 3 4 5
    good | T T F F F

class SVNRepo:
    @classmethod
    ___ isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""


class Solution:
    ___ findFirstBadVersion(self, n
        """
        :type n: int
        :rtype: int
        """
        __ not n:
            r_ 0

        left, right = 1, n
        w___ left + 1 < right:
            mid = (left + right) // 2
            __ isBadVersion(mid
                right = mid
            ____
                left = mid

        r_ left __ isBadVersion(left) else right
