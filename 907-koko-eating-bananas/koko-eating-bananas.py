class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def count( speed ) : 
            hours = 0 
            for pile in piles : 
                hours += pile // speed
                if pile%speed != 0 :
                    hours += 1
            return hours

        l = 1
        r = max(piles)
        result = max(piles)
        while l<=r: 
            speed = (l+r) // 2
            hours = count(speed)
            if hours > h :
                l = speed + 1
            else:
                result = min(result, speed)
                r = speed - 1

        return result