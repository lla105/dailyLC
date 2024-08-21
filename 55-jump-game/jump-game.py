class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0

        for i in range(len(nums)):
            if gas < 0:
                return False
            elif gas < nums[i]:
                gas = nums[i]
            gas-=1
        return True