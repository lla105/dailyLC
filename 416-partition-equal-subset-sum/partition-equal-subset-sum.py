class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        


        arrsum = sum(nums)
        t = arrsum//2
        # print( ' ta?rget : ', t)
        dp = [False] * ( t +1 )
        dp[0] = True
        # print(11.1%1 )
        # print(11%1)
        if (arrsum/2)%1!=0:
            return False

        for num in nums:
            for i in range( t, -1, -1) :
                # print( num, i)
                if i>=num and dp[i-num]:
                    dp[i] = True
                    # print(dp)

        return dp[-1]
