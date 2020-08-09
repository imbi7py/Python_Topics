#!/usr/bin/python3
"""
premium question
"""

# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ __init__(self
        self.sums = []

    ___ checkEqualTree(self, root: TreeNode) -> bool:
        """
        To save 2nd pass, store sums
        space: O(N)
        """
        self.dfs(root)
        total = self.sums.pop()
        r_ total % 2 __ 0 and total // 2 in self.sums

    ___ dfs(self, node
        __ not node:
            r_ 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        s = l + r + node.val
        self.sums.append(s)
        r_ s


class Solution:
    ___ __init__(self
        """
        Save space, two passes
        """
        self.exists = False
        self.root = None  # need to handle 0
        self.total_sum = None

    ___ checkEqualTree(self, root: TreeNode) -> bool:
        """
        two passes
        1st pass, get total sum
        2nd pass, check whether has sum/2
        space: O(log N)

        To save 2nd pass, store sums
        space: O(N)
        """
        self.root = root
        self.total_sum = self.dfs(root)
        self.dfs(root)
        r_ self.exists

    ___ dfs(self, node
        __ not node:
            r_ 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        s = l + r + node.val
        __ node != self.root and self.total_sum != None and self.total_sum __ s * 2:
            self.exists = True

        r_ s
