class Solution(object
  ___ compareVersion(self, version1, version2
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split(".")
    v2 = version2.split(".")
    i = 0
    w___ i < le.(v1) and i < le.(v2
      v1Seg, v2Seg = int(v1[i]), int(v2[i])
      __ v1Seg > v2Seg:
        r_ 1
      ____ v1Seg < v2Seg:
        r_ -1
      ____
        i += 1
    __ i < le.(v1) and int("".join(v1[i:])) != 0:
      r_ 1
    __ i < le.(v2) and int("".join(v2[i:])) != 0:
      r_ -1
    r_ 0
