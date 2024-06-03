class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

# eg amount = 11$
# coins = [1,2,5]

# arr = [0 , 0, 0, 0, ....,0] <- least coins req for each$
#        0 , 1, 2, 3, 4, 5, 6, 7
# arr = [0 , 1, 1, 2, 2, 1

# coins[i] must be <= arr[i] 
        arr = [ float('inf') ] * (amount+1)
        arr[0] = 0
        # arr[1] = 1
        for i in range(len(arr)):
            # print(i)
            for j in range(len(coins)):
                if coins[j] <= i:
                    # print(' coin: ', coins[j])
                    tempmin = arr[i-coins[j]] + 1
                    arr[i] = min(arr[i], tempmin)
            # print(" arr: ", arr)
        if type(arr[-1]) is not float:
            return arr[-1]
        else:
            return -1