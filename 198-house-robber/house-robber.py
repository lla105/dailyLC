class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[-1]
        if len(nums)==2:
            return max(nums[0] , nums[1])
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max( nums[2]+dp[0] , nums[1] )

        for i in range(3,len(nums)):
            prevsum1 = dp[i-1]
            prevsum2 = dp[i-2] + nums[i]
            prevsum3 = dp[i-3] + nums[i]
            dp[i] = max(prevsum1 , prevsum2, prevsum3)

        print(dp)

        return max(dp[-1], dp[-2])