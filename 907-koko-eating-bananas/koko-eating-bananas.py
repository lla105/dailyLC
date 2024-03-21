class Solution:
    def minEatingSpeed(self, piles: List[int], hr: int) -> int:
        print(piles)
        def findtotal(k,piles):
            res=0
            for pile in piles:
            
                if pile%k==0:
                    res+=pile/k
                else:
                    res+=(pile//k)+1
            return res
        h = max(piles)
        l=1
        minimumk=float('inf')
        while l<=h:
            
            mid=(l+h)//2
            t=findtotal(mid,piles)
            if  t<=hr:
                minimumk = min(minimumk,mid)
                h=mid-1
            else:
                l=mid+1
        return minimumk