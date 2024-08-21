class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        l = 0
        r = len(height) - 1

        while l<r:
            curh = min(height[l] , height[r])
            curw = r-l
            maxwater = max(curh*curw , maxwater)
            if height[l] > height[r] : 
                r-=1
            else:
                l+=1
        return maxwater