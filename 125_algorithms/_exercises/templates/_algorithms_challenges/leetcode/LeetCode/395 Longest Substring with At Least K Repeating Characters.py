"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every
character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ longestSubstring(self, s, k
        """
        D & C, forming boundary by the letter of min count
        :type s: str
        :type k: int
        :rtype: int
        """
        __ not s:
            r_ 0

        cnt = defaultdict(int)
        for e in s: cnt[e] += 1

        c = min(
            s,
            key=lambda x: cnt[x],
        )

        __ cnt[c] >= k:
            r_ le.(s)

        r_ max(
            map(lambda x: self.longestSubstring(x, k), s.split(c))
        )
