#!/usr/bin/python3
"""
Return the root node of a binary search tree that matches the given preorder
traversal.

(Recall that a binary search tree is a binary tree where for every node, any
descendant of node.left has a value < node.val, and any descendant of node.right
has a value > node.val.  Also recall that a preorder traversal displays the
value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note:
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
from typing ______ List


# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        """
        need to be BST

        scan the list to break left and right part
        F(n) = 2 F(n/2) + O(n), then it is O(n log n)

        Make it O(n)
        maintain a stack
        After walking through example, left child can be determined quickly
        since it is pre-order. Left comes first.

        Stack maintain a node that is missing right child
        decreasing stack
        """
        root = TreeNode(preorder[0])
        stk = [root]
        ___ a in preorder[1:]:
            node = TreeNode(a)
            __ a < stk[-1].val:  # le.(stk) always >= 1
                stk[-1].left = node
            ____
                w___ le.(stk) >= 2 and stk[-2].val < a:
                    stk.p..

                stk[-1].right = node
                stk.p..

            stk.append(node)

        r_ root

    ___ bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        If a node is a right child (larger), find the proper parent
        The proper parent should the deepest in the stack that its val < current val
        """
        root = TreeNode(preorder[0])
        stk = [root]
        ___ a in preorder[1:]:
            node = TreeNode(a)
            __ a < stk[-1].val:
                stk[-1].left = node
            ____
                w___ stk and stk[-1].val < a:
                    pi = stk.p..
                pi.right = node
            stk.append(node)
            
        r_ root
