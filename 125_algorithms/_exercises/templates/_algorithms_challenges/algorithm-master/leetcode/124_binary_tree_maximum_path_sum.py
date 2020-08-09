"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ maxPathSum(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_ 0

        ans, _ = self.divide_conquer(root)
        r_ ans

    ___ divide_conquer(self, node
        __ not node:
            r_ float('-inf'), 0

        max_left, left = self.divide_conquer(node.left)
        max_right, right = self.divide_conquer(node.right)

        # 0 means discard the negative path
        res = max(max_left, max_right, node.val + left + right)
        path = max(node.val + left, node.val + right, 0)

        r_ res, path


class Solution:
    ___ maxPathSum(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_ 0

        self.ans = float('-inf')
        self.divide_conquer(root)
        r_ self.ans

    ___ divide_conquer(self, node
        __ not node:
            r_ 0

        left = max(0, self.divide_conquer(node.left))
        right = max(0, self.divide_conquer(node.right))

        __ node.val + left + right > self.ans:
            self.ans = node.val + left + right

        r_ node.val + max(left, right)
