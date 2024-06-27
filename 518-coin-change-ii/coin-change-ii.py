class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] *(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(amount+1):
                if coin <= i:
                    dp[i] += dp[i-coin]
                # print('   ', dp)
        # print(dp)
        return dp[-1]
        # self.s = set()
        # self.result = 0
        # def bf(curList, index):
        #     # print('1)  ', sum(curList) , curList, amount)
        #     if sum(curList) == amount:
        #         temps = tuple(sorted(curList))
        #         # print('  2)  MATCH : ', tuple(temps))
        #         if temps not in self.s:
        #             # print('    3) append to result')
        #             self.result+=1
        #             self.s.add(temps)
        #         return
        #     if sum(curList) > amount:
        #         return
            
        #     for i in range(index, len(coins)):
        #         coin = coins[i]
        #         # print(i, coin, curList)
        #         bf(curList+[coin], i)
        #     return
        # bf( [] , 0 )

        # return self.result
