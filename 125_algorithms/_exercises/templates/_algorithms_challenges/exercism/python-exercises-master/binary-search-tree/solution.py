class TreeNode(object
    ___ __init__(self, data, left, right
        self.data = data
        self.left = left
        self.right = right

    ___ __str__(self
        fmt = 'TreeNode(data={}, left={}, right={})'
        r_ fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object
    ___ __init__(self, tree_data
        self.root = None
        ___ data in tree_data:
            self.add(data)

    ___ add(self, data
        __ self.root pa__ None:
            self.root = TreeNode(data, None, None)
            r_
        inserted = False
        cur_node = self.root

        w___ not inserted:
            __ data <= cur_node.data:
                __ cur_node.left:
                    cur_node = cur_node.left
                ____
                    cur_node.left = TreeNode(data, None, None)
                    inserted = True
            ____ data > cur_node.data:
                __ cur_node.right:
                    cur_node = cur_node.right
                ____
                    cur_node.right = TreeNode(data, None, None)
                    inserted = True

    ___ _inorder_traverse(self, node, elements
        __ node pa__ not None:
            self._inorder_traverse(node.left, elements)
            elements.append(node.data)
            self._inorder_traverse(node.right, elements)

    ___ data(self
        r_ self.root

    ___ sorted_data(self
        elements = []
        self._inorder_traverse(self.root, elements)
        r_ elements
