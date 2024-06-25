class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp = sum(nums)
        if temp%2!=0:
            return False
        target = temp//2
        dp = [ False ] *(target+1)
        dp[0] = True


        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]
                