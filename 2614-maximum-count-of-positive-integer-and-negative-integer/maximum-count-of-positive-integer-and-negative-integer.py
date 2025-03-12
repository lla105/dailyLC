class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ncount = 0
        pcount = 0
        for i in range(len(nums)):
            if nums[i] > 0 :
                pcount += 1
            elif nums[i] < 0 :
                ncount += 1
        return max(pcount, ncount)