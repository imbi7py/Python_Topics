'''
Created on Mar 23, 2017

@author: MT
'''

class Solution(object
    ___ countNumbersWithUniqueDigits(self, n
        __ n __ 0: r_ 1
        res = 10
        uniqueDigits = 9
        availableNumbers = 9
        w___ n > 1 and availableNumbers > 0:
            uniqueDigits = uniqueDigits*availableNumbers
            res += uniqueDigits
            availableNumbers -= 1
            n -= 1
        r_ res
