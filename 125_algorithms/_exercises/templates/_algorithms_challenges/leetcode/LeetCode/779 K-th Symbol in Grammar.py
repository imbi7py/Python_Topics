#!/usr/bin/python3
"""
On the first row, we write a 0. Now in every subsequent row, we look at the
previous row and replace each occurrence of 0 with 01, and each occurrence of 1
with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of
K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""


class Solution:
    ___ kthGrammar(self, N: int, K: int) -> int:
        """
        pattern

           0
          0 1
         01  10
        0110 1001
        recursive go thorugh the pattern
        """
        r_ self.dfs(N, K, True)

    ___ dfs(self, N, K, not_flip
        __ N __ 1:
            r_ 0 __ not_flip else 1
        half_l = 2 ** (N - 1) // 2
        __ K <= half_l:
            r_ self.dfs(N - 1, K, not_flip)
        ____
            r_ self.dfs(N - 1, K - half_l, not not_flip)

    ___ kthGrammar_TLE(self, N: int, K: int) -> int:
        """
        Find pattern
        Precedence: Logic < Bitwise < Arithmetic operator < Unary

           0
          0 1
         01  10
        0110 1001
        Generating the actual string will TLE
        """
        row = 0
        pos = 1
        for n in range(1, N
            row = (row << pos) + (~row & 2 ** pos - 1)
            pos *= 2

        ret = row >> pos - K & 1
        r_ ret


__ __name__ __ "__main__":
    assert Solution().kthGrammar(1, 1) __ 0
    assert Solution().kthGrammar(2, 1) __ 0
    assert Solution().kthGrammar(2, 2) __ 1
    assert Solution().kthGrammar(4, 5) __ 1
