class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[-1]
        if len(nums)==2:
            return max(nums[0] , nums[1])

        dp = []
        for i in range(len(nums)):
            dp.append(0)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[1] , nums[2]+dp[0])
        # print("DP: ", dp)
        # print("nums: ", nums)
        for i in range(3, len(nums)):
            # print(f'{i} : max( {dp[i-2]}+{nums[i]} , {dp[i-1]}')
            dp[i] = max(dp[i-2]+nums[i] , dp[i-1], dp[i-3]+nums[i])
        print(dp)
        # print(dp[-1] , dp[-2])
        # print(max(dp[-1], dp[-2ll]))
        return max(dp[-1] , dp[-2])
