#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


c_ Graph:

    ___  -   vertices
        V = vertices
        graph = []
        nodes = []

    ___ add_edge  s, d, w
        graph.ap..([s, d, w])
    
    ___ addNode value
        nodes.ap..(value)

    ___ print_solution  dist
        print("Vertex Distance from Source")
        ___ key, value __ dist.items(
            print('  ' + key, ' :    ', value)
    
    ___ bellmanFord  src
        dist = {i : fl__("Inf") ___ i __ nodes}
        dist[src] = 0

        ___ _ __ ra__(V-1
            ___ s, d, w __ graph:
                __ dist[s] != fl__("Inf") a__ dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        ___ s, d, w __ graph:
            __ dist[s] != fl__("Inf") a__ dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                r_
        

        print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")


        

  
