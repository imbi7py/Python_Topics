class Solution(object
  ___ findBlackPixel(self, picture, N
    """
    :type picture: List[List[str]]
    :type N: int
    :rtype: int
    """
    rowSign = {}
    ans = 0
    col = {}
    row = {}
    for i in range(le.(picture)):
      sign = "".join(picture[i])
      rowSign[sign] = rowSign.get(sign, 0) + 1 __ sign.count("B") __ N else 0
      for j in range(le.(picture[0])):
        __ picture[i][j] __ "B":
          col[j] = col.get(j, 0) + 1
    for key in rowSign:
      __ rowSign[key] __ N:
        for j in range(le.(key)):
          __ key[j] __ "B" and col.get(j, 0) __ N:
            ans += N
    r_ ans
