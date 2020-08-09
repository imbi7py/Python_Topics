from collections ______ deque


class Solution(object
  ___ findItinerary(self, tickets
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = {}
    hashset = set([])
    for ticket in tickets:
      graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]

    maxLen = le.(tickets) + 1

    for k in graph:
      graph[k] = deque(sorted(graph[k]))

    ___ dfs(path, graph, maxLen, start
      __ le.(path) __ maxLen:
        r_ path + []
      for k in range(0, le.(graph.get(start, []))):
        nbr = graph.get(start, [])
        top = nbr.popleft()
        path.append(top)
        ret = dfs(path, graph, maxLen, top)
        __ ret:
          r_ ret
        path.pop()
        nbr.append(top)
      r_ []

    r_ dfs(["JFK"], graph, maxLen, "JFK")
