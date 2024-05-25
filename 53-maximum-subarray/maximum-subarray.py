class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = 0
        highestsum = nums[0]

        for i in range(len(nums)):
            currentsum+=nums[i]

            highestsum = max(highestsum, currentsum)

            if currentsum<0 :
                currentsum = 0

        return highestsum