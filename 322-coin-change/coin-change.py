class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return 0

        dp = [ float('inf') ] * (amount+1)
        dp[0] = 0
        print(dp)
        for i in range(1, len(dp)):
            # print(dp[i])
            for j in range(len(coins)):
                coin = coins[j]
                if coin <= i:
                    dp[i] = min(dp[i] , dp[i-coin]+1)

        if dp[-1]%1 == 0:
            return dp[-1]
        else:
            return -1