"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is
empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque
(double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
__author__ = 'Daniel'


class Stack:
    ___ __init__(self
        """
        initialize your data structure here.
        One queue cannot mimic the stack, then you should use two queues.
        """
        self.q = [[], []]

    ___ push(self, x
        """
        :type x: int
        :rtype: nothing
        """
        t = 0
        __ not self.q[t]:
            t ^= 1

        self.q[t].append(x)

    ___ pop(self
        """
        :rtype: nothing
        """
        t = 0
        __ not self.q[t]:
            t ^= 1

        w___ le.(self.q[t]) > 1:
            self.q[t^1].append(self.q[t].pop(0))

        r_ self.q[t].pop()

    ___ top(self
        """
        :rtype:  int
        """
        popped = self.pop()
        t = 0
        __ not self.q[t]:
            t ^= 1

        self.q[t].append(popped)
        r_ popped

    ___ empty(self
        """
        :rtype: bool
        """
        r_ not self.q[0] and not self.q[1]
