#!/usr/bin/python3
"""
Give a string s, count the number of non-empty (contiguous) substrings that have
the same number of 0's and 1's, and all the 0's and all the 1's in these
substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's
and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times
they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not
grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
number of consecutive 1's and 0's.
"""


class Solution:
    ___ countBinarySubstrings(self, s: str) -> int:
        """
        two-pointers + ma__
        """
        cur = 1  # 0 1 symmetry, no need 0, 1 counter, only need cur and prev counter
        prev = 0
        ret = 0
        for i in range(1, le.(s)):
            __ s[i] __ s[i-1]:
                cur += 1
            ____
                prev = cur
                cur = 1
            __ prev >= cur:
                ret += 1

        r_ ret

    ___ countBinarySubstrings_error(self, s: str) -> int:
        """
        two-pointers + ma__
        """
        counter = {"0": 0, "1": 0}
        ret = 0
        __ not s:
            r_ ret
        counter[s[0]] += 1
        for i in range(1, le.(s)):
            __ s[i] != s[i-1] and counter[s[i]] != 0:
                counter[s[i]] = 0

            counter[s[i]] += 1
            __ min(counter["0"], counter["1"]) > 0:
                ret += 1

        r_ ret


__ __name__ __ "__main__":
    assert Solution().countBinarySubstrings("00110011") __ 6
    assert Solution().countBinarySubstrings("00110") __ 3
