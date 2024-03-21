def countspeed(piles, speed):
    hours = 0
    for p in piles:
        hours += math.ceil(p/speed)
    return hours

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left<=right:
            mid = (left+right)//2
            turnsUsed = countspeed(piles, mid)

            if turnsUsed<=h:
                result = min(result, mid)
                right=mid-1
            else:
                left=mid+1


        return result
        