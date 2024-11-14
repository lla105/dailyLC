class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tempsum = 0
        maxsum = nums[0]

        for i in range(len(nums)):
            num = nums[i]
            tempsum += num
            maxsum = max(maxsum, tempsum)
            if tempsum<0:
                tempsum = 0
        return maxsum