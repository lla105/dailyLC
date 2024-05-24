class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #[-2,1,-3,4,-1,2,1,-5,4]
        #[-2,1,1, 4,4 ,5,6, 6,6]
        highest = nums[0]
        current = 0

        for i in range(len(nums)):
            current += nums[i]
            if current > highest:
                highest = current
            if current < 0:
                current = 0
        return highest