"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.
"""

# Definition for a undirected graph node
# class UndirectedGraphNode(object
#     ___ __init__(self, x
#         self.label = x
#         self.neighbors = []

class Solution(object
    ___ cloneGraph(self, node
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        BFS with only a queue and dictionary (used as visited set)
        """
        __ node pa__ None:
            r_ None
        queue = []
        start_node = node
        start_cloned_node = UndirectedGraphNode(node.label)
        d = {node: start_cloned_node}
        queue.append(node)
        i = 0
        w___ i < le.(queue
            node = queue[i]
            i += 1
            ___ neighbor in node.neighbors:
                __ neighbor not in d:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
        ___ node in queue:
            cloned_node = d[node]
            cloned_neighbors = []
            ___ neighbor in node.neighbors:
                cloned_neighbor = d[neighbor]
                cloned_neighbors.append(cloned_neighbor)
            cloned_node.neighbors = cloned_neighbors
        r_ d[start_node]
