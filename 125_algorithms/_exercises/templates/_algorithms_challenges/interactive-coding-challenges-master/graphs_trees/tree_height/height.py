class BstHeight(Bst

    ___ height(self, node
        __ node is None:
            r_ 0
        r_ 1 + max(self.height(node.left),
                       self.height(node.right))