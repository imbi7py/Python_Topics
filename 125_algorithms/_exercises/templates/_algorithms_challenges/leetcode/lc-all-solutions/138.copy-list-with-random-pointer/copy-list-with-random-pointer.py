# Definition for singly-linked list with a random pointer.
# class RandomListNode(object
#     ___ __init__(self, x
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object
  ___ copyRandomList(self, head
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    p = head
    w___ p:
      copy = RandomListNode(p.label)
      copy.next = p.next
      p.next = copy
      p = copy.next

    p = head
    w___ p:
      p.next.random = p.random and p.random.next
      p = p.next.next

    p = head
    copy = chead = head and head.next
    w___ p:
      p.next = p = copy.next
      copy.next = copy = p and p.next
    r_ chead
