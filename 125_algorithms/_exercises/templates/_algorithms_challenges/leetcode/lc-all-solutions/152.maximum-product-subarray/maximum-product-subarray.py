class Solution(object
  ___ maxProduct(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    maxDP = [0 for _ in range(0, le.(nums))]
    minDP = [0 for _ in range(0, le.(nums))]
    maxDP[0] = nums[0]
    minDP[0] = nums[0]
    ans = nums[0]
    for i in range(1, le.(nums)):
      maxDP[i] = max(minDP[i - 1] * nums[i], nums[i], maxDP[i - 1] * nums[i])
      minDP[i] = min(minDP[i - 1] * nums[i], maxDP[i - 1] * nums[i], nums[i])
      ans = max(ans, maxDP[i])
    r_ ans
