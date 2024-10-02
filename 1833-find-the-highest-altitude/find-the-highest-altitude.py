class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        sum2 = 0
        for g in gain:
            sum2 += g
            highest = max(highest, sum2)
        return highest