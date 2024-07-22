class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxsum = nums[0]
        cursum = 0

        for i in range(len(nums)):
            cursum += nums[i]
            maxsum = max(maxsum, cursum)
            if cursum < 0 :
                cursum = 0

        return maxsum