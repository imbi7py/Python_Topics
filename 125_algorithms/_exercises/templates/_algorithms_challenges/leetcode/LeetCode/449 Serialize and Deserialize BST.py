"""
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is
no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary search tree can be serialized to a string
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""


# Definition for a binary tree node.
class TreeNode(object
  ___ __init__(self, x
      self.val = x
      self.left = None
      self.right = None


class Codec:
    DELIMITER = ","

    ___ serialize(self, root
        """Encodes a tree to a single string.
        Basic binary tree serialize (BFS), see Serialize and Deserialize
        Binary Tree

        The main difference is as compact as possible. No need "null", since
        insertion order is specfied.

            3 (1)
        2 (2)  5 (2)
                 6 (3)  # bracket () is the insertion order

        pre-order traversal keeps the insertion order
        :type root: TreeNode
        :rtype: str
        """
        ___ traverse(root, ret
            __ not root:
                r_

            ret.append(root.val)
            traverse(root.left, ret)
            traverse(root.right, ret)

        ret = []
        traverse(root, ret)
        r_ self.DELIMITER.join(map(str, ret))

    ___ deserialize(self, data
        """Decodes your encoded data to tree.

        Normal BST insert
        :type data: str
        :rtype: TreeNode
        """
        __ not data:
            r_
            
        lst = list(map(int, data.split(self.DELIMITER)))
        root = TreeNode(lst[0])
        ___ insert(root, val
            # need to keep the parent
            __ val < root.val:
                __ not root.left:
                    root.left = TreeNode(val)
                ____
                    insert(root.left, val)
            ____
                __ not root.right:
                    root.right = TreeNode(val)
                ____
                    insert(root.right, val)

        for a in lst[1:]:
            insert(root, a)

        r_ root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
