class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(height) - 1
        while l<r :
            cur_vol = min(height[l],height[r]) * (r-l)
            max_vol = max(max_vol , cur_vol )
            if height[l] > height[r] :
                r -= 1
            else:
                l += 1
        return max_vol

        #height = [1,8,6,2,5,4,8,3,7]
        # 0 : min(1,7)*8 = 8
        # 1 : min(8,7)*7 = 49
        # 2 : min(8,3)*6 = 18
        # 3 : min(8,8)*5 = 40

        #height = [1,1]
        # 0 : min(1,1)*1 = 1

        #height = [1,x,2] > [1,2]=w*1 > 
        # move the lower height pointer. 
        #height = [ ,l,r] : if x lower: take x, if x higher, take r (higher value)
        #height = [l,r, ] : if x lower: take x, if x higher, take l (lower value)