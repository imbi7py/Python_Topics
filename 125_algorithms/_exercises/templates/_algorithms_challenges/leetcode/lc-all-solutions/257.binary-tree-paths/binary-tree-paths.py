# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {string[]}
  ___ binaryTreePaths(self, root
    ___ helper(root, path, res
      __ root:
        path.append(str(root.val))
        left = helper(root.left, path, res)
        right = helper(root.right, path, res)
        __ not left and not right:
          res.append("->".join(path))
        path.p..
        r_ True

    res = []
    helper(root, [], res)
    r_ res
