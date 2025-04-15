class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        curSum  = 0
        maxSum = float('-inf')
        for r in range(len(nums)):
            while curSum < 0 and l<r:
                curSum -= nums[l]
                l+=1
            curNum = nums[r]
            curSum += curNum
            maxSum = max( maxSum, curSum )

        return maxSum
            