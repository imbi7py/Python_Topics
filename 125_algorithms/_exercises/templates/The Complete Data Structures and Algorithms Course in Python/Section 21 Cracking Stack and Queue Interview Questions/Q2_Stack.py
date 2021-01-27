#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
  
#   Create Stack with min method

class Node(
    ___ __init__(self, value=None, next = None
        self.value = value
        self.next = next
    
    ___ __str__(self
        string = str(self.value)
        __ self.next:
            string += ',' + str(self.next)
        return string

class Stack(
    ___ __init__(self
        self.top = None
        self.minNode = None
    
    ___ min(self
        __ not self.minNode:
            return None
        return self.minNode.value
    
    ___ push(self, item
        __ self.minNode and (self.minNode.value < item
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        ____
            self.minNode = Node(value = item, next=self.minNode)
        self.top = Node(value=item, next=self.top)
    
    ___ pop(self
        __ not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item

customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())

