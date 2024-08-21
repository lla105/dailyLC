class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = nums[0]
        spot = 0
        while gas > 0 and spot<len(nums):
            gas -= 1
            spot += 1
            if spot>=len(nums)-1:
                return True
            gas = max(gas, nums[spot])

        if spot>=len(nums)-1:
            return True
        else:
            return False