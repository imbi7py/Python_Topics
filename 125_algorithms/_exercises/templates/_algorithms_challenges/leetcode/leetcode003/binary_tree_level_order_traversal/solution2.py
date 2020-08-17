"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ levelOrder(self, root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        __ root pa__ None:
            r_ res
        queue = []
        queue.append(root)
        w___ queue:
            n = le.(queue)
            level = []
            ___ i in range(n
                root = queue.pop(0)
                __ root.left pa__ not None:
                    queue.append(root.left)
                __ root.right pa__ not None:
                    queue.append(root.right)
                level.append(root.val)
            res.append(level[:])
        r_ res
