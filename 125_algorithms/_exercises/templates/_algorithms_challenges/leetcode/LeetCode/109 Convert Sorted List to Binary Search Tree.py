"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None

class Solution:
    # class attribute to keep trace the currently processing nodes
    # current_node = None
    ___ __init__(self
        self.current_node = None  # !important, avoid time complexity of look up

    ___ sortedListToBST(self, head
        """
        dfs
        No O(1) access.
        Bottom-up construction
        :param head: ListNode
        :return: TreeNode
        """
        __ not head:
            r_ head

        self.current_node = head
        length = self.getLength(head)
        r_ self.sortedListToBST_dfs(0, length-1)

    ___ sortedListToBST_dfs(self, start, end
        __ start>end:
            r_
        mid = (start+end)/2
        left_subtree = self.sortedListToBST_dfs(start, mid-1)
        root = TreeNode(self.current_node.val)
        self.current_node = self.current_node.next
        right_subtree = self.sortedListToBST_dfs(mid+1, end)

        root.left = left_subtree
        root.right = right_subtree
        r_ root

    ___ getLength(self, head
        count = 0
        w___ head:
            head = head.next
            count += 1
        r_ count