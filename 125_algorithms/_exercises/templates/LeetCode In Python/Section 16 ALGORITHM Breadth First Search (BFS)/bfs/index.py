
from collections ______ defaultdict


c_ Graph:

    ___ __init__(
        .graph _ defaultdict(list)

    ___ setEdge(, u, v
        .graph[u].append(v)

    ___ bfs(, s
        visited _ set()

        queue _ []
        queue.append(s)

        visited.add(s)

        w___ queue:
            u _ queue.pop(0)
            print(u, end_" ")

            ___ v __ .graph[u]:
                __ v not __ visited:
                    queue.append(v)
                    visited.add(v)


g _ Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.bfs(2)
