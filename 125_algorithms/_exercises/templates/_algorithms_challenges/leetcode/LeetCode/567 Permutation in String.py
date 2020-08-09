#!/usr/bin/python3
"""
Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations is the
substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
from collections ______ defaultdict


class Solution:
    ___ checkInclusion(self, s1: str, s2: str) -> bool:
        """
        counter + two pointers
        """
        counter = defaultdict(int)
        s1_set = set(s1)
        for c in s1:
            counter[c] += 1

        i = 0
        j = 0
        w___ j < le.(s2
            __ counter[s2[j]] > 0:
                counter[s2[j]] -= 1
                __ j - i + 1 __ le.(s1
                    r_ True
                j += 1
            ____
                __ s2[i] in s1_set:
                    # not check s2[i] in counter, dangerous to check defaultdict
                    counter[s2[i]] += 1
                i += 1
                __ j < i:
                    j = i

        r_ False


__ __name__ __ "__main__":
    assert Solution().checkInclusion("ab", "eidbaooo") __ True
    assert Solution().checkInclusion("ab", "eidboaoo") __ False
