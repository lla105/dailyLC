class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber( arr ) :
            if len(arr) < 3:
                return [max(arr)]
            dp = [ float('inf') ] * len(arr) 
            dp[0] = arr[0]
            dp[1] = arr[1] 
            dp[2] = max(arr[2]+dp[0] , dp[1])
            for i in range( 3, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i])
            return dp

        if len(nums) == 1:
            return nums[0]

        route1 = nums[:-1]
        route2 = nums[1:]
        dp1 = robber(route1)
        dp2 = robber(route2)

        print(dp1)
        print(dp2)
        return max(dp1[-1] , dp2[-1])
