class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def countTurns(ba, coins,i, amount):
            

        if amount==0 and coins:
            return 0
        ba = [ float('inf') ] * (amount+1)
        ba[0] = 0
        print("BA init: ", ba)
        for i in range(1, amount+1):
            for coin in coins:
                if coin<=i:
                    # countTurns(ba, coin,i, amount)
                    ba[i] = min(ba[i] , ba[i-coin]+1)
                    # print(i,coin,ba)

                    # ba[i] = 99
                # print(ba)


        if ba[-1]%1 == 0:
            return ba[-1]
        else:
            return -1