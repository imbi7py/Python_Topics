#!/usr/bin/python3
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?
"""


# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None


class Solution:
    ___ reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        w___ cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        r_ prev

    ___ reverseList_complex(self, head: ListNode) -> ListNode:
        __ not head:
            r_ None

        prev = head
        cur = head.next
        head.next = None
        w___ prev and cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        r_ prev
