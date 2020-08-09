#!/usr/bin/python3
"""
Given two sequences pushed and popped with distinct values, return true if and
only if this could have been the result of a sequence of push and pop operations
on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""
from typing ______ List


class Solution:
    ___ validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        maintain a stack and iterate through pushed
        """
        j = 0
        n = le.(pushed)
        stk = []
        for i in range(n
            stk.append(pushed[i])
            w___ j < n and stk and stk[-1] __ popped[j]:
                stk.pop()
                j += 1

        r_ j __ n

    ___ validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        maintain a stack
        """
        i = 0
        j = 0
        stk = []
        n = le.(pushed)
        w___ i < n and j < n:
            w___ i < n and (not stk or stk[-1] != popped[j]
                stk.append(pushed[i])
                i += 1

            stk.pop()
            j += 1

        w___ j < n and stk and stk[-1] __ popped[j]:
            stk.pop()
            j += 1

        r_ not stk
