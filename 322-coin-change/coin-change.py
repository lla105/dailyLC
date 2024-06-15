class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # print('did not catch 0')
        # amount  = 10
        # coins = [2,3,9]
        LeastCoin = [ float('inf') ] * (amount+1)
        LeastCoin[0] = 0
        # print(LeastCoin)

        for i in range( 1, amount+1) :
            # print(i,") ")
            for coin in coins : 
                if coin <= i :
                    LeastCoin[i] = min(LeastCoin[i] , LeastCoin[i - coin] + 1)
                    # numberA = LeastCoin[i]
                    # numberB = LeastCoin[i - coin] + 1
                    # smallerNumber = min(numberA, numberB)
                    # LeastCoin[i] = smallerNumber
        # print(LeastCoin)
        # return LeastCoin[-1]
        if LeastCoin[-1] % 1 != 0 :
            # is a float
            return -1
        else:
            return LeastCoin[-1]