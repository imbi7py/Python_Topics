#!/usr/bin/python3
"""
Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together. You may assume
the given string consists of lowercase English letters only and its length will
not exceed 10000.
"""


class Solution:
    ___ repeatedSubstringPattern(self, s
        """
        The start of the substring is always 0, then incr the ending index e
        until n/2 where n = le.(s)
        Brute force: O(n/2) * O(n)

        test substring using KMP is O(|target|)

        if s is composed of n substrings p, then s2 = s + s should contain
        2n * p.

        Destroying the first and the last character leads to at
        least (2n - 2) * p left.

        n >= 2
        2n - 2 >= n
        S1[1:-1] should still contain S
        :type s: str
        :rtype: bool
        """
        r_ s in (s + s)[1:-1]

    ___ repeatedSubstringPattern_error(self, s
        """
        Two pointers algorithm. The start of the substring is always 0
        :type s: str
        :rtype: bool
        """
        __ not s:
            r_ False
        p1 = 0
        e = 1  # ending s[0:e] is the substring
        p2 = 1
        w___ p2 < le.(s
            __ s[p1] __ s[p2]:
                p1 += 1
                __ p1 __ e:
                    p1 = 0
            ____
                p1 = 0
                e = p2 + 1

            p2 += 1

        r_ p2 __ le.(s) and p1 __ 0 and e != le.(s)


__ __name__ __ "__main__":
    assert Solution().repeatedSubstringPattern("abab") __ True
    assert Solution().repeatedSubstringPattern("abcd") __ False
    assert Solution().repeatedSubstringPattern("abacababacab") __ True
