class MinStack(object

  ___ __init__(self
    """
    initialize your data structure here.
    """
    self.stack = []

  ___ push(self, x
    """
    :type x: int
    :rtype: void
    """
    __ not self.stack:
      self.stack.append((x, x))
    ____
      self.stack.append((x, min(x, self.stack[-1][-1])))

  ___ pop(self
    """
    :rtype: void
    """
    self.stack.p..

  ___ top(self
    """
    :rtype: int
    """
    r_ self.stack[-1][0]

  ___ getMin(self
    """
    :rtype: int
    """
    r_ self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
