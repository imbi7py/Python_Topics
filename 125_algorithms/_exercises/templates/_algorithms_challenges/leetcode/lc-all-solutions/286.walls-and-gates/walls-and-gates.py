from collections ______ deque

INF = 2147483647


class Solution(object
  ___ wallsAndGates(self, rooms
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    queue = deque([])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(0, le.(rooms)):
      for j in range(0, le.(rooms[0])):
        __ rooms[i][j] __ 0:
          queue.append((i, j))

    w___ queue:
      i, j = queue.popleft()
      for di, dj in directions:
        p, q = i + di, j + dj
        __ 0 <= p < le.(rooms) and 0 <= q < le.(rooms[0]) and rooms[p][q] __ INF:
          rooms[p][q] = rooms[i][j] + 1
          queue.append((p, q))
