# Path Sum
# Question: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example: Given the below binary tree and sum = 22,
# 5
# / \
# 4 8
# / / \
# 11 13 4
# / \ \
# 7 2 1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Solutions:


c_ TreeNode:
    ___  - , x:
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    ___ hasPathSum , root, su.:
        __ root __ N..:
            # Empty tree will always result in False
            r_ F..
        ____ root.left __ N.. an. root.right __ N..:
            # Reach the leaf.
            r_ root.val __ su.
        ____ root.left __ N..:
            # Only has right child.
            r_ hasPathSum root.right, su.-root.val
        ____ root.right __ N..:
            # Only has left child.
            r_ hasPathSum root.left, su.-root.val
        ____
            # Has two children.
            r_ hasPathSum root.left, su.-root.val o. hasPathSum root.right, su.-root.val


__  -n __ '__main__':
    BT, BT.right, BT.right.left, BT.left _ TreeNode 1, TreeNode 2, TreeNode 3, TreeNode 10
    print   Solution .hasPathSum BT, 6