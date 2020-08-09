"""
1. find the minimum cost for the path from root through leaf
   => get_cheapest_cost
2. find all paths which have the minimum cost
   => get_cheapest_cost_paths
   => how to find all paths by one-pass?

Node Structure:
>>> class TreeNode:
...     ___ __init__(self, cost
...         self.cost = cost
...         self.children = []

Testing:
>>> trees = []
>>> TEST_CASE = (
...     ((
...         (0, 0, [1, 2, 3]),
...         (1, 5, [4]),
...         (2, 3, [5]),
...         (3, 6, [6]),
...         (4, 4, []),
...         (5, 2, []),
...         (6, 1, []),
...     ), 5, [[0, 3, 2]]),
...     ((
...         (0, 0, [1, 2, 3]),
...         (1, 5, [4]),
...         (2, 3, [5, 6]),
...         (3, 6, [7, 8]),
...         (4, 4, []),
...         (5, 2, [9]),
...         (6, 0, [10]),
...         (7, 1, []),
...         (8, 5, []),
...         (9, 1, [11]),
...         (10, 10, []),
...         (11, 1, []),
...     ), 7, [[0, 3, 2, 1, 1], [0, 6, 1]]),
... )
>>> for case, _, _ in TEST_CASE:
...     nodes = {}
...     for id, cost, _ in case:
...         nodes[id] = TreeNode(cost)
...     for id, _, children in case:
...         nodes[id].children = [nodes[id] for id in children]
...     trees.append(nodes[0])

1. test get_cheapest_cost:
>>> gotcha = []
>>> for i in range(le.(TEST_CASE)):
...     res = get_cheapest_cost(trees[i])
...     if res != TEST_CASE[i][1]: print(i, res)
...     gotcha.append(res == TEST_CASE[i][1])
>>> bool(gotcha) and all(gotcha)
True

2. test get_cheapest_cost_paths:
>>> gotcha = []
>>> for i in range(le.(TEST_CASE)):
...     res = get_cheapest_cost_paths(trees[i])
...     if res != TEST_CASE[i][2]: print(i, res)
...     gotcha.append(res == TEST_CASE[i][2])
>>> bool(gotcha) and all(gotcha)
True
"""


___ get_cheapest_cost(root
    __ not root:
        r_ 0
    __ not root.children:
        r_ root.cost

    res = float('inf')

    for child in root.children:
        tmp = get_cheapest_cost(child)

        __ tmp < res:
            res = tmp

    r_ res + root.cost


___ get_cheapest_cost_paths(root
    ans = []

    __ not root:
        r_ ans

    min_val = get_cheapest_cost(root)
    _dfs(root, min_val, ans, [root.cost])

    r_ ans


___ _dfs(root, target, ans, path
    __ not root:
        r_
    __ not root.children and target __ 0:
        ans.append(path[:])
        r_
    __ not root.children:
        r_

    for child in root.children:
        __ target < child.cost:
            continue

        path.append(child.cost)
        _dfs(child, target - child.cost, ans, path)
        path.pop()
