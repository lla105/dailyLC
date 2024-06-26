class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[-1]
        if len(nums)==2:
            return max(nums[0] , nums[1])
        dp = [0] * (len(nums) )
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            print(i)
            house1 = dp[i-1]
            house2 = nums[i] + dp[i-2]
            house3 = nums[i] + dp[i-3]
            dp[i] = max(house1, house2, house3)
        print(dp)
        return max(dp[-1] , dp[-2])
