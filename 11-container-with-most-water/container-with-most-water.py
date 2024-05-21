class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = float('-inf')

        l = 0
        r = len(height)-1
        while l<r:
            currheight = min(height[l] , height[r])
            currArea = currheight*(r-l)
            answer = max(answer, currArea)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return answer