class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [ float('inf') ] * (len(cost) + 1) 
        # dp[-1] = min(cost[-1] , cost[-2] )
        # dp[-1] = 0
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = min( cost[i]+cost[i+1] , cost[i]+cost[i+2])
        return min(cost[0] , cost[1])