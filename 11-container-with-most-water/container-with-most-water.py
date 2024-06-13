class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0 

        l = 0
        r = len(height) - 1
        while l<r:
            curvol = (r-l) * min(height[l] , height[r])
            maxvol = max(maxvol , curvol)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxvol