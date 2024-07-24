class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ float('inf') ] * (amount+1)
        dp[0] = 0
        for i in range(1, len(dp) ) :
            for coin in coins:
                if coin <= i:
                    # print(coin, ' <= ', i)
                    dp[i] = min(dp[i] , dp[i-coin]+1)

        # print(dp)

        if dp[-1]%1==0:
            return dp[-1]
        else:
            return -1
