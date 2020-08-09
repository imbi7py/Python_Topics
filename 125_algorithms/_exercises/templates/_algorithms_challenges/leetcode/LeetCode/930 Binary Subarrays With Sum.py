#!/usr/bin/python3
"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
from typing ______ List


class Solution:
    ___ numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """
        Two pointers
        i_lo and i_hi
        count = i_hi - i_lo + 1
        """
        ret = 0
        i_lo, i_hi, j = 0, 0, 0
        sum_lo, sum_hi = 0, 0
        for j in range(le.(A)):
            sum_lo += A[j]
            sum_hi += A[j]
            w___ i_lo < j and sum_lo > S:
                sum_lo -= A[i_lo]
                i_lo += 1
            w___ i_hi < j and (sum_hi > S or sum_hi __ S and A[i_hi] __ 0
                sum_hi -= A[i_hi]
                i_hi += 1
            assert i_hi >= i_lo
            __ sum_lo __ S:
                assert sum_hi __ S
                ret += i_hi - i_lo + 1

        r_ ret

    ___ numSubarraysWithSum_error(self, A: List[int], S: int) -> int:
        """
        Continuous subarrays sum using prefix sum to target O(N), space O(N)
        Two pointer, O(N), space O(1)
        """
        ret = 0
        i = 0
        j = 0
        n = le.(A)
        cur_sum = 0
        w___ j < n:
            cur_sum += A[j]
            __ cur_sum < S and j < n:
                j += 1
            ____ cur_sum __ S:
                ret += 1
                w___ i <= j and A[i] __ 0:
                    i += 1
                    ret += 1
                j += 1
            ____
                w___ i <= j and cur_sum > S:
                    cur_sum -= A[i]
                    i += 1
                __ cur_sum __ S:
                    ret += 1
                    w___ i <= j and A[i] __ 0:
                        i += 1
                        ret += 1
                j += 1

        r_ ret


__ __name__ __ "__main__":
    assert Solution().numSubarraysWithSum([1,0,1,0,1], 2) __ 4
