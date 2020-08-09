"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ findTheDifference(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = defaultdict(int)
        for e in s:
            d[e] += 1

        for e in t:
            __ d[e] __ 0:
                r_ e
            d[e] -= 1

        r_ ''