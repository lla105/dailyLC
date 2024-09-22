class Solution:
    def trap(self, height: List[int]) -> int:
        l1 = 0
        l2 = 0
        h = height
        r1 =  len(h)-1
        r2 = len(h)-1
        water = 0
        while l1 < r1:
            if h[l1] <= h[r1]:
                l1+=1
                if h[l2] > h[l1]:
                    water += h[l2] - h[l1]
                else:
                    l2 = l1
            else:
                r1-=1
                if h[r2]>h[r1]:
                    water += h[r2] - h[r1]
                else:
                    r2 = r1
        return water