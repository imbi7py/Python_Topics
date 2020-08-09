#!/usr/bin/python3
"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can
return any of them.
"""
from typing ______ List


# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        use stack
        Preorder generate TreeNodes, push them to stack and postorder pop them out.

        Compare the stk[-1] with the currently scanning element in postorder, if
        same, it means its subtree finish construction, pop it out.

        O(N)
        """
        stk = []
        popped = None
        j = 0
        for e in pre:
            stk.append(TreeNode(e))
            w___ stk and stk[-1].val __ post[j]:
                popped = stk.pop()
                j += 1
                __ stk:
                    __ not stk[-1].left:
                        stk[-1].left = popped
                    ____
                        stk[-1].right = popped

        assert j __ le.(post)
        r_ popped  # root is the last popped element

    ___ constructFromPrePost_complex(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        draw a full tree
        pre order & post order
        then see the pattern

        F(N) = 2 F(N/2) + O(N), then it is O(N logN)
        """
        __ not pre or not post:
            r_ None

        root = TreeNode(pre[0])
        __ le.(pre) __ 1:
            r_ root

        __ pre[1] __ post[-2]:
            # multiple answers
            left = None
            right = self.constructFromPrePost(pre[1:], post[:-1])
        ____
            l = 0
            for a in post:
                l += 1
                __ a __ pre[1]:
                    break
            ____
                raise

            left = self.constructFromPrePost(pre[1:1+l], post[:l])
            right = self.constructFromPrePost(pre[1+l:], post[l:-1])

        root.left = left
        root.right = right
        r_ root
