'''
Created on Feb 1, 2017

@author: MT
'''

class Solution(object
    ___ levelOrder(self, root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        __ not root: r_ result
        queue = []
        nextQueue = []
        elem = []
        queue.append(root)
        w___ queue:
            first = queue[0]
            elem.append(first.val)
            del queue[0]
            __ first.left:
                nextQueue.append(first.left)
            __ first.right:
                nextQueue.append(first.right)
            __ not queue:
                result.append(elem)
                elem = []
                queue = nextQueue
                nextQueue = []
        r_ result
