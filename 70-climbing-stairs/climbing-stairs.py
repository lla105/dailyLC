class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0 :
            return 0
        if n == 2:
            return 2
        if n == 1:
            return 1
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        # print(dp)
        
        return dp[n]
