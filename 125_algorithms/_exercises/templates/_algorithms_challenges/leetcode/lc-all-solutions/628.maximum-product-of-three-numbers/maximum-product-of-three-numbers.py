class Solution(object
  ___ maximumProduct(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    r_ max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
