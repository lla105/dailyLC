class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [ float('inf') ] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i<coin:
                    continue
                dp[i] = min(dp[i] , dp[i-coin]+1)
        print(dp)

        # return dp[-1]
        if dp[-1]%1 != 0:
            return -1
        else:
            return dp[-1]
