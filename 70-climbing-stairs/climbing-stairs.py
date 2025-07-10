class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [ float('inf') ] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n) :
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

#trav(0)
#   trav(1) 
#       trav(2)
#           trav(3)
#           trav(4)
#       trav(3)
#   trav(2)
#       trav(3)
#       trav(4)

# n = 2
# [1,1], [2]
# n = 3
# [1,1,1], [1,2], [2,1]

# Decisions: at each step, either:
# a) take 1 step
# b) take 2 steps
#[1]
#   [1,1]
#       [1,1,1]
#       [1,1,2]
#   [1,2]
#       [1,2,1]
#       [1,2,2]
#[2]
#   [2,1]
#       [2,1,1]
#       [2,1,2]
#   [2,2]
#       [2,2,1]
#       [2,2,2]