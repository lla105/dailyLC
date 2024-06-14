class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ float('inf') ] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i] = min(dp[i] , dp[i-coin]+1)
        if dp[-1]%1 !=0 :
            return -1
        else:
            return dp[-1]


        # target = amount
        # self.answer = float('inf')
        # self.lastusedcoin = 0
        # self.usedcoins = set()
        # def trav(coinindex, cursum, coincount):
        #     print('1 New stack :', coinindex, cursum, coincount)
        #     print('1.1 usedcoin: ', self.lastusedcoin)
        #     if coins[coinindex]>coins[-1] or self.lastusedcoin>=len(coins):
        #         print(' 2 Coin index over, returning')
        #         return
        #     if cursum>target:
        #         print('  3 cursum > target. returning')
        #         return
        #     if cursum == target:
        #         self.answer = min(self.answer, coincount)
        #         print('   4 curusm==target! self.answer = ', self.answer)
        #     for i in range(self.lastusedcoin, len(coins)):
        #         trav(i, cursum+coins[i], coincount+1)
        #     self.usedcoins.add(self.lastusedcoin)
        #     self.lastusedcoin += 1
        #     print('     5 end stack. returning')
        # trav(0, 0, 0)
        # if self.answer%1!=0:
        #     return -1
        # else:
        #     return self.answer