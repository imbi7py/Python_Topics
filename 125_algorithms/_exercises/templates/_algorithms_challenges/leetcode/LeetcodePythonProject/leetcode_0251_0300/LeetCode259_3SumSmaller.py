'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object
    ___ threeSumSmaller(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(le.(nums)-2
            j, k = i+1, le.(nums)-1
            w___ j < k:
                __ nums[i]+nums[j]+nums[k] >= target:
                    k -= 1
                ____
                    res += k-j
                    j += 1
        r_ res
    
    ___ test(self
        testCases = [
            ([-2, 0, 1, 3], 2),
            ([3, 1, 0, -2], 4),
        ]
        for nums, target in testCases:
            print('nums: %s' % (nums))
            print('target: %s' % (target))
            result = self.threeSumSmaller(nums, target)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
