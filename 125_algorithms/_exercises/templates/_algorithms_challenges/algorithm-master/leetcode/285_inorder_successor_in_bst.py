"""
Definition for a binary tree node.
>>> class TreeNode:
...     ___ __init__(self, x
...         self.val = x
...         self.left = None
...         self.right = None
...         self.parent = None

>>> trees = []
>>> tree_infos = [
...     ((
...         (1, None, None, 2),
...         (2, 1, None, None),
...     ), '1,2'),
...     ((
...         (20, None, 8, 22),
...         (8, 20, 4, 12),
...         (22, 20, None, None),
...         (4, 8, None, None),
...         (12, 8, 10, 14),
...         (10, 12, None, None),
...         (14, 12, None, None),
...     ), '4,8,10,12,14,20,22'),
...     ((
...         (10, None, 5, 100),
...         (5, 10, None, None),
...         (100, 10, 80, 120),
...         (80, 100, None, None),
...         (120, 100, None, None),
...     ), '5,10,80,100,120'),
...     ((
...         (1, None, None, 2),
...         (2, 1, None, 3),
...         (3, 2, None, 4),
...         (4, 3, None, 5),
...         (5, 4, None, 6),
...         (6, 5, None, 7),
...         (7, 6, None, None),
...     ), '1,2,3,4,5,6,7'),
... ]

>>> for info, _ in tree_infos:
...     nodes = {node[0]: TreeNode(node[0]) for node in info}
...
...     for val, parent, left, right in info:
...         if parent:
...             nodes[val].parent = nodes[parent]
...         if left:
...             nodes[val].left = nodes[left]
...         if right:
...             nodes[val].right = nodes[right]
...
...     trees.append(nodes[info[0][0]])

>>> gotcha = []
>>> for _in, _out in (
...     ((trees[0], trees[0]), trees[0].right),
...     ((trees[1], trees[1].left.right.right), trees[1]),
...
...     for s in (Solution(), Solution2(), Solution3(), Solution4()):
...         res = s.inorderSuccessor(*_in)
...         if res is not _out: print(_in[0].val, res.val)
...         gotcha.append(res is _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    """
    time: O(log n) or O(h), `n` is the number of nodes and `h` is the tree height

    1. if `target` has right child, then successor lies at the most-left child in right child of `target`
    2. otherwise, just traverse down from root, and record `ans` when every time go left
    """
    ___ inorderSuccessor(self, root, target
        """
        :type root: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        __ not root or not target:
            r_

        ans = None

        __ target.right:
            ans = target.right
            w___ ans and ans.left:
                ans = ans.left
            r_ ans

        w___ root and target.val != root.val:
            __ target.val < root.val:
                ans = root
                root = root.left
            ____
                root = root.right

        r_ ans


class Solution2:
    """
    time: O(n), `n` is the number of nodes

    just do inorder traverse
    """
    ___ inorderSuccessor(self, root, target
        """
        :type root: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        __ not root or not target:
            r_

        stack = []
        node = root
        got_target = False

        w___ node or stack:
            w___ node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            __ got_target:
                r_ node
            __ node.val __ target.val:
                got_target = True

            node = node.right


class Solution3:
    """
    * every node has `parent` pointer
    time: O(log n) or O(h), `n` is the number of nodes and `h` is the tree height

    1. if `target` has right child, then successor lies at the most-left child in right child of `target`
    2. otherwise, just traverse top to root
    """
    ___ inorderSuccessor(self, root, target
        """
        :type root: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        __ not root or not target:
            r_

        ans = None

        __ target.right:
            ans = target.right
            w___ ans and ans.left:
                ans = ans.left
            r_ ans

        ans = target.parent
        w___ ans and target is ans.right:
            target = ans
            ans = ans.parent

        r_ ans


class Solution4:
    """
    * every node has `parent` pointer
    time: O(log n) or O(h), `n` is the number of nodes and `h` is the tree height

    1. if `target` has right child, then successor lies at the most-left child in right child of `target`
    2. otherwise, just traverse top to root
    """
    ___ inorderSuccessor(self, root, target
        """
        :type root: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        __ not root or not target:
            r_

        __ target.right:
            ans = target.right
            w___ ans and ans.left:
                ans = ans.left
            r_ ans

        ans = target.parent
        w___ ans and ans.val < target.val:
            ans = ans.parent

        r_ ans
