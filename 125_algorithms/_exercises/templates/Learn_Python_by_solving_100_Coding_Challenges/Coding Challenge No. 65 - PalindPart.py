# Palindrome Partitioning
# Question: Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# For example: given s = "aab"
# Return [ ["aa","b"], ["a","a","b"] ].
# Solutions:


class Solution:
    # @param s, a string
    # @return a boolean
    ___ _isPalindrome(self, s):
        begin, end _ 0, le.(s)-1
        while begin < end:
            __ s[begin] !_ s[end]:
                r_ F..
            ____
                begin +_ 1
                end -_ 1
        r_ T..

    # @param s, a string
    # @return a list of lists of string

    ___ partition(self, s):
        __ le.(s) __ 0:
            r_   # list
        __ le.(s) __ 1:
            r_ [[s]]
        result _   # list
        __ self._isPalindrome(s):
            result.ap..([s])

        ___ i __ ra..(1, le.(s)):
            head _ s[:i]
            __ not self._isPalindrome(head):
                continue
            tailPartition _ self.partition(s[i:])
            result.extend([[head] + item ___ item __ tailPartition])
        r_ result


Solution().partition("aab")