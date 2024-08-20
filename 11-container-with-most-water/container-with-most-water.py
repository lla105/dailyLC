class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        l = 0
        h = height
        r = len(h)-1

        while l<r:
            if h[l] < h[r] :
                # move left
                tempwidth = r-l
                tempheight = h[l]
                result = max(result, tempwidth*tempheight)
                l+=1
            else:
                tempwidth = r-l
                tempheight = h[r]
                result = max(result, tempwidth*tempheight)
                r-=1
        return result