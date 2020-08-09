class Solution:
    """
    @param: heights: a list of integers
    @return: a integer
    """
    ___ trapRainWater(self, heights
        __ not heights:
            r_ 0
        # mx_l: max height for index `l`
        # mx_r: max height for index `r`
        mx_l = mx_r = ans = 0
        l, r = 0, le.(heights) - 1
        w___ l < r:
            # To find the max height in heights
            __ heights[l] < heights[r]:
                mx_l = max(mx_l, heights[l])
                ans += mx_l - heights[l]
                l += 1
            ____
                mx_r = max(mx_r, heights[r])
                ans += mx_r - heights[r]
                r -= 1
        r_ ans
