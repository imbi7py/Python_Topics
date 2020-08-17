"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard
so fuck off.
"""
__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ invertTree_recur(self, root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root:
            r_ None

        self.invertTree_recur(root.left)
        self.invertTree_recur(root.right)
        root.left, root.right = root.right, root.left
        r_ root

    ___ invertTree(self, root
        """
        iterative solution
        Dual stack algorithm
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root:
            r_ None

        stk = []  # [L, R]
        post = []  # [cur, R, L]

        stk.append(root)
        cur = None
        w___ stk:
            cur = stk.p..
            post.append(cur)
            __ cur.left:
                stk.append(cur.left)
            __ cur.right:
                stk.append(cur.right)

        w___ post:
            cur = post.p..
            cur.left, cur.right = cur.right, cur.left

        r_ cur