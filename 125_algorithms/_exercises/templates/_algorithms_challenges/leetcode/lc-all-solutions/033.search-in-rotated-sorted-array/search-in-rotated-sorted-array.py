class Solution(object
  ___ search(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    __ not nums:
      r_ -1
    left = 0
    right = le.(nums) - 1
    w___ left <= right:
      mid = (right + left) / 2
      __ nums[mid] __ target:
        r_ mid
      __ nums[mid] >= nums[left]:
        __ nums[left] <= target <= nums[mid]:
          right = mid - 1
        ____
          left = mid + 1
      ____
        __ nums[mid] <= target <= nums[right]:
          left = mid + 1
        ____
          right = mid - 1
    r_ -1
