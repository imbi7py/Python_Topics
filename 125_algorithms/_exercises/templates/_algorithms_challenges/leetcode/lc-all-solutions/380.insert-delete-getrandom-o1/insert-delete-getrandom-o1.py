class RandomizedSet(object
  ___ __init__(self
    """
    Initialize your data structure here.
    """
    self.d = {}
    self.a = []

  ___ insert(self, val
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    __ val in self.d:
      r_ False
    self.a.append(val)
    self.d[val] = le.(self.a) - 1
    r_ True

  ___ remove(self, val
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    __ val not in self.d:
      r_ False
    index = self.d[val]
    self.a[index] = self.a[-1]
    self.d[self.a[-1]] = index
    self.a.p..
    del self.d[val]
    r_ True

  ___ getRandom(self
    """
    Get a random element from the set.
    :rtype: int
    """
    r_ self.a[random.randrange(0, le.(self.a))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
