class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        output = 0
        cache = [0] * (len(cost))
        cache[-1] = cost[-1]
        cache[-2] = cost[-2]
        #cost = [0,1,2,3]
        #cache= [0,1,2,3]
        print(cache)
        for i in range( len(cost)-3, -1, -1 ) :
            cache[i] = min(cost[i]+cache[i+1] , cost[i]+cache[i+2])
        return min(cache[0], cache[1])

# Decisions: take 1 or 2 steps

#10
#   +15
#       +20
#           end
#       end
#   +20
#       end
#15
#   +20
#       end
#   end

# cost = [1,100,1000,1]
# cost = [1,1000,100,1]
# cache= [x,x,   100,1]