class Solution:
    def maxArea(self, height: List[int]) -> int:
        # print(f'{height}')
        maxArea = 0
        left = 0
        right = len(height)-1

        while left<right:
            #pick the shorter bar
            h = min(height[left], height[right])
            currArea = h * (right-left)
            maxArea = max(maxArea, currArea)

            #remember to append left or right
            if height[left] > height[right]:
                right = right -1
            else:
                left = left + 1
        return maxArea