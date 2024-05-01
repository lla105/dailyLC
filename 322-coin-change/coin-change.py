class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [ float('inf') ] * (amount+1)
        arr[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin<=i:
                    # print(i, coin)
                    arr[i] = min( arr[i] , arr[i-coin] + 1 )
        if arr[-1] % 1 != 0 :
            return -1
        else:
            return arr[-1]