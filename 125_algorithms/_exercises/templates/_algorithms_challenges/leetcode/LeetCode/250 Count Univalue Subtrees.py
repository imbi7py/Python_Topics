"""
Premium Question
"""

__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ __init__(self
        self.cnt = 0

    ___ countUnivalSubtrees(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        self.is_unival(root)
        r_ self.cnt

    ___ is_unival(self, cur
        __ not cur:
            r_ True

        is_left = self.is_unival(cur.left)
        is_right = self.is_unival(cur.right)  # attention to test condition shortcut
        __ (not is_left or not is_right or
                    cur.left and cur.left.val != cur.val or
                    cur.right and cur.right.val != cur.val
            r_ False
        ____
            self.cnt += 1  # for currently visiting node as the root of subtree.
            r_ True
