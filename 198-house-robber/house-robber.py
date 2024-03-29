class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return nums[-1]
        if len(nums)==2: return max(nums[-1], nums[-2])
        # if len(nums)==0 return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[2]+dp[0] , dp[1])
        
        result = 0
        for i in range(3, len(nums)):
            # print(i)
            dp[i] = max(nums[i]+dp[i-2] , nums[i]+dp[i-3] , dp[i-1])


        print(dp)

        return max(dp[-2] , dp[-1])
