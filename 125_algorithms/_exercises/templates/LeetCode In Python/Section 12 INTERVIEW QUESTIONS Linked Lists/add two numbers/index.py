# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

c_ Solution:
    ___ addTwoNumbers l1: ListNode, l2: ListNode)  ListNode:
        ans _ ListNode(N..)
        pointer _ ans

        carry _ 0
        su. _ 0

        w___(l1!_None o.. l2!_None
            su. _ carry
            __(l1!_None
                su.+_l1.val
                l1 _ l1.n..
            __(l2!_None
                su.+_l2.val
                l2 _ l2.val
            
            carry _ in.(su./10)
            pointer.n..  _ ListNode(su.%10)

            pointer _ pointer.n..
        
        __(carry>0
            pointer.n.. _ ListNode(carry)
        
        r_ ans.n..