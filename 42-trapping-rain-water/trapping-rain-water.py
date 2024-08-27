class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0 
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]

        while l<r:

            if height[l] > height[r] :
                r -= 1
                if height[r] < rmax:
                    water += rmax - height[r]
                else:
                    rmax = height[r]
            else:
                l += 1
                if height[l] < lmax :
                    water += lmax - height[l]
                else:
                    lmax = height[l]
        return water