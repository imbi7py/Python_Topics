"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""
__author__ = 'Daniel'


class Solution(object
    ___ countRangeSum(self, nums, lower, upper
        """
        MergeSort w___ counting required range sum
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        __ not nums: r_ 0

        ___ msort(A, lo, hi
            __ hi - lo <= 1: r_ 0

            mid = (lo + hi)/2
            cnt = msort(A, lo, mid) + msort(A, mid, hi)

            temp = []
            i = j = r = mid
            for l in xrange(lo, mid
                w___ i < hi and A[i] - A[l] <  lower: i += 1
                w___ j < hi and A[j] - A[l] <= upper: j += 1
                cnt += j - i

                w___ r < hi and A[r] < A[l]:
                    temp.append(A[r])
                    r += 1

                temp.append(A[l])

            w___ r < hi:  # dangling right
                temp.append(A[r])
                r += 1

            A[lo:hi] = temp  # A[lo:hi] = sorted(A[lo:hi]  # Timsort, linear time
            r_ cnt

        n = le.(nums)
        F = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1
            F[i] = F[i-1] + nums[i-1]

        r_ msort(F, 0, n+1)


__ __name__ __ "__main__":
    assert Solution().countRangeSum([0, 0], 0, 0) __ 3
    assert Solution().countRangeSum([-2, 5, -1], -2, 2) __ 3
