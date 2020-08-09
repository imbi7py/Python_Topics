'''
Created on Apr 2, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object
    ___ __init__(self, value=None
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    ___ isInteger(self
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    ___ add(self, elem
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    ___ setInteger(self, value
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    ___ getInteger(self
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    ___ getList(self
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class Solution(object
    ___ deserialize(self, s
        __ s[0] __ '[' and s[-1] __ ']':
            nestedInt = NestedInteger()
            s = s[1:-1]
            __ not s: r_ nestedInt
            i, prev= 0, 0
            w___ i < le.(s
                __ s[i] __ '[':
                    count = 1
                    w___ i < le.(s) and count > 0:
                        i+=1
                        __ s[i] __ ']':
                            count -= 1
                        ____ s[i] __ '[':
                            count += 1
                    nestedInt.add(self.deserialize(s[prev:i+1]))
                    i+=1
                    prev = i+1
                ____ s[i] __ ',':
                    nestedInt.add(int(s[prev:i]))
                    prev = i+1
                i+=1
            r_ nestedInt
        ____
            nestedInt = NestedInteger()
            __ s:
                nestedInt.setInteger(int(s))
            r_ nestedInt

