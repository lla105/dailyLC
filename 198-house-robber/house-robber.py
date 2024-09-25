class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(dp)):
            if i==2:
                dp[i] = nums[i] + dp[i-2]
                # print('>>> ' , nums[i] , dp[i-2])
                continue
            dp[i] = max( nums[i]+dp[i-3] , nums[i]+dp[i-2] )
            # print( dp, nums[i]+dp[i-3] , nums[i]+dp[i-2] )
        return max(dp[-1], dp[-2])