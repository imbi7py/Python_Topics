"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""
__author__ = 'Daniel'


class Solution:
    ___ rotate(self, nums, k
        """
        in place
        """
        n = le.(nums)
        k %= n
        temp = nums[:n-k]
        for i in xrange(n
            __ i < k:
                nums[i] = nums[n-k+i]
            ____
                nums[i] = temp[i-k]

