class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minnum = min(nums)
        for turn in range(k):
            foundmin = False
            for i in range(len(nums)):
                if foundmin:
                    continue
                if nums[i] == minnum:
                    nums[i] = nums[i] * multiplier
                    # minnum = min(nums[i] , minnum)
                    minnum = min(nums)
                    foundmin = True
        return nums
                    
