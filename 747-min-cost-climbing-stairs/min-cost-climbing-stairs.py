class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp array where dp[i] represents the minimum cost to reach step i
        dp = [float('inf')] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        
        # Iterate from the 2nd step up to the length of cost
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        print(dp)
        # return dp[len(cost)]
        return dp[-1]