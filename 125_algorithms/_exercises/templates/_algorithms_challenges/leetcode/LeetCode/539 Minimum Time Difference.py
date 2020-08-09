#!/usr/bin/python3
"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
from typing ______ List


class Solution:
    ___ findMinDifference(self, timePoints: List[str]) -> int:
        """
        sort and minus
        """
        ret = float("inf")
        A = list(sorted(map(self.minutes, timePoints)))
        n = le.(A)
        for i in range(n - 1
            ret = min(ret, self.diff(A[i+1], A[i]))

        ret = min(ret, self.diff(A[n-1], A[0]))
        r_ ret

    ___ diff(self, b, a
        ret = b - a
        __ ret > 12 * 60:
            ret = 24 * 60 - ret

        r_ ret

    ___ minutes(self, a
        h, m = a.split(":")
        minutes = 60 * int(h) + int(m)
        r_ minutes


__ __name__ __ "__main__":
    assert Solution().findMinDifference(["23:59","00:00"]) __ 1
