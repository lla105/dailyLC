class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        target = totalsum /2
        if totalsum%1 != 0:
            return False
        if target%1 != 0:
            return False
        target = int(target)
        dp = [False] * ( int(target) +1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]

        return dp[target]