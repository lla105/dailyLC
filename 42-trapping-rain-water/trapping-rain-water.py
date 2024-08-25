class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = height[left]
        rightmax = height[right]
        water = 0
        while left < right:
            if leftmax < rightmax :
                left+=1
                leftmax = max(leftmax, height[left])
                water += abs(height[left] - leftmax)
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                water += abs(height[right] - rightmax)
        return water