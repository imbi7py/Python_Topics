'''
Created on Mar 14, 2017

@author: MT
'''

class Solution(object
    ___ longestValidParentheses(self, s
        left = -1
        stack = []
        res = 0
        for i, c in enumerate(s
            __ c __ '(':
                stack.append(i)
            ____
                __ stack:
                    stack.pop()
                    __ stack:
                        res = max(res, i-stack[-1])
                    ____
                        res = max(res, i-left)
                ____
                    left = i
        r_ res
    
    ___ test(self
        testCases = [
            '()',
            '(()',
            ')()())',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.longestValidParentheses(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
