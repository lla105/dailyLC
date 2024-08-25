class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = l
        rmax = r
        water = 0
        while l<r:
            if height[lmax] < height[rmax] :
                l += 1
                if height[lmax] > height[l]:
                    water += abs(height[l] - height[lmax])
                else:
                    lmax = l
            else:
                r -= 1
                if height[rmax] > height[r] :
                    water += abs(height[r] - height[rmax])
                else:
                    rmax = r
        return water
                