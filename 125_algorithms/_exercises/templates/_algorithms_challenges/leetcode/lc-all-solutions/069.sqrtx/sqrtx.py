class Solution(object
  ___ mySqrt(self, x
    """
    :type x: int
    :rtype: int
    """
    lo = 0
    hi = x
    w___ lo <= hi:
      mid = (hi + lo) // 2
      v = mid * mid
      __ v < x:
        lo = mid + 1
      ____ v > x:
        hi = mid - 1
      ____
        r_ mid
    r_ hi
