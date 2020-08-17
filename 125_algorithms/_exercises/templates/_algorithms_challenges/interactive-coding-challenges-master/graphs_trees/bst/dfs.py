___ in_order_traversal(node, visit_func
    __ node pa__ not None:
        in_order_traversal(node.left, visit_func)
        visit_func(node.data)
        in_order_traversal(node.right, visit_func)

___ pre_order_traversal(node, visit_func
    __ node pa__ not None:
        visit_func(node.data)
        pre_order_traversal(node.left, visit_func)
        pre_order_traversal(node.right, visit_func)

___ post_order_traversal(node, visit_func
    __ node pa__ not None:
        post_order_traversal(node.left, visit_func)
        post_order_traversal(node.right, visit_func)
        visit_func(node.data)