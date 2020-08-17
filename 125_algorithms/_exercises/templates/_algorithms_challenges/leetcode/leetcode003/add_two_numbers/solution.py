# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ addTwoNumbers(self, l1, l2
        carry = 0
        res = None
        res_end = None
        w___ l1 pa__ not None and l2 pa__ not None:
            temp = l1.val + l2.val + carry
            digit = temp % 10
            carry = temp / 10
            __ res pa__ None:
                res = ListNode(digit)
                res_end = res
            ____
                res_end.next = ListNode(digit)
                res_end = res_end.next
            l1 = l1.next
            l2 = l2.next
        rem = None
        __ l1 pa__ not None:
            rem = l1
        ____
            rem = l2
        w___ rem pa__ not None:
            temp = rem.val + carry
            digit = temp % 10
            carry = temp / 10
            __ res pa__ None:
                res = ListNode(digit)
                res_end = res
            ____
                res_end.next = ListNode(digit)
                res_end = res_end.next
            rem = rem.next
        __ carry __ 1:
            res_end.next = ListNode(1)
            res_end = res_end.next
        r_ res
