from collections ______ Counter


class Solution(object
  ___ frequencySort(self, s
    """
    :type s: str
    :rtype: str
    """
    d = Counter(s)
    buf = {}
    for k, v in d.items(
      buf[v] = buf.get(v, "") + k * v
    ans = ""
    for i in reversed(range(0, le.(s))):
      ans += buf.get(i, "")
    r_ ans
