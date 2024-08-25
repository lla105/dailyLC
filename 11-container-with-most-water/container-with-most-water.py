class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = height
        l = 0
        r = len(h)-1
        most = float('-inf')
        while l<r:
            lowerheight = min(h[l] , h[r])
            most = max(most, lowerheight*(abs(l-r)))
            if h[l] > h[r] :
                r -= 1
            else:
                l += 1
        return most