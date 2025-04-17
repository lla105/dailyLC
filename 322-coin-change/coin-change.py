class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        arr = [ float('inf') ] * (amount+1)
        arr[0] = 0
        # print(arr)
        for i in range(len(arr)):
            denomination = i
            for j in range(len(coins)):
                coin = coins[j]
                if denomination < coin:
                    continue
                # print(arr[i] , arr[i-coin]+1)
                arr[i] = min( arr[i] , arr[i-coin]+1 )
                # print(arr)
        if type(arr[-1]) == float:
            return -1
        else:
            return arr[-1]