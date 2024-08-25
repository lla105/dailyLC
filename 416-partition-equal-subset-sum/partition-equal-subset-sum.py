class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp format = [T,F,F,F,F,F,F] len(nums)//2
        numsum = sum(nums)
        target = numsum//2
        print(numsum%2)
        if numsum%2 != 0 :
            return False
        dp = [False]* (target+1)
        dp[0] = True

        for num in nums:
            for i in range( target, -1, -1 ):
                if i+num<len(dp) and dp[i]:
                    dp[i+num] = True
        print(dp)
        return dp[-1]