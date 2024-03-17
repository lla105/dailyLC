class Solution:
    def maxArea(self, height: List[int]) -> int:
        # print(height)
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right: 
            print(f'left: {left}')
            lefth = height[left]
            righth = height[right]

            curheight = min(lefth, righth)
            curArea = (right-left) * curheight
            maxArea = max(curArea, maxArea)

            if lefth > righth:
                right -= 1
            else:
                left += 1

        return maxArea