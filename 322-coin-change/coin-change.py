class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.cache = [ float('inf') ] * (amount+1)
        self.cache[0] = 0

        #cache = [0,inf,inf,inf,inf,inf] , amount = 5
        for i in range(len(self.cache)):
            for j in range(len(coins)):
                coin = coins[j]
                if coin>i :
                    continue
                self.cache[i] = min(self.cache[i] , self.cache[i-coin]+1 )
        print(self.cache)
        if type(self.cache[-1] % 1) == int:
            return self.cache[-1]
        else:
            return -1
# cache = [a,b,c,d,e]

# Redundencies:
# 1) coin orders shouldn't matter (1,2) vs (2,1)
#   solution: coins[i] from coin[start_idx]
# xxxx 2) reaching same leftover number: (1,1,1,1,1) vs (5)
#amount=11 , coins=[1,2,5]
# cache = [inf,inf,inf,...,inf] , len(cache)=amount
# cache = [1,2/1, ]
# return cache[-1]

#1  2   3   4   5
#1
#   1,1
#       1,1,1
#           1,1,1,1
#               1,1,1,1,1
#       1,2
#           1,2,2
#               1,2,2,1
#   2
#       2,1
#           2,2
#               2,2,1
#               5

#1,10
#   1,9
#       1,8
#           1,7
#               ... 1,0 (base case) 
#       2,7
#       5,4
#   2,8
#   5,5
#2,9
#   x1,8
#   2,7
#   5,4
#5,6