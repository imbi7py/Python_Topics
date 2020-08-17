# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     ___ __init__(self, x
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    ___ copyRandomList(self, head
        __ head pa__ None:
            r_ None
        h = head
        p = h
        w___ p pa__ not None:
            next_node = p.next
            new_node = RandomListNode(p.label)
            # Insert new node to the original list
            p.next = new_node
            new_node.next = next_node
            p = next_node
        p = h
        w___ p pa__ not None:
            next_node = p.next.next
            new_node = p.next
            __ p.random pa__ not None:
                new_node.random = p.random.next
            p = next_node
        # Split the list
        res = None
        end = None
        p = h
        w___ p pa__ not None:
            next_node = p.next.next
            new_node = p.next
            # Add to new list
            __ res pa__ None:
                res = new_node
                end = new_node
            ____
                end.next = new_node
                end = end.next
            # Delete new node from old list
            p.next = next_node
            p = next_node
        r_ res
