"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
    ___ hasCycle(self, head
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        w___ fast pa__ not None and fast.next pa__ not None:
            slow = slow.next
            fast = fast.next.next
            __ slow __ fast:
                r_ True
        r_ False
