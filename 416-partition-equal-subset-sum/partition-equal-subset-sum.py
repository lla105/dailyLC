class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        half = totalsum / 2
        print( ' half : ', half)
        if half%1 != 0:
            return False
        target = totalsum // 2

        dp = [ False ] * (target + 1)
        dp[0] = True
        print( ' target : ', target)
        for num in nums :
            for i in range(target , -1, -1 ):
                if  i+num<len(dp) and dp[i] :
                    dp[i+num] = True
        print(dp)

        return dp[-1]
