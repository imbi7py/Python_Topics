#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 4 - Sum Lists

from LinkedList import LinkedList

___ sumList(llA, llB
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    w__ n1 or n2:
        result = carry
        __ n1:
            result += n1.value
            n1 = n1.next
        __ n2:
            result += n2.value
            n2 = n2.next
        ll.add(in.(result % 10))
        carry = result / 10
    
    r_ ll

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA, llB))
