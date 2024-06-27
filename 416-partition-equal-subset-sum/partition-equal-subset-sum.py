class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tempsum = sum(nums)
        target = tempsum // 2
        if tempsum%2!=0:
            return False
        self.isPossible = False
        dp = [False] * (target+1 )
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        print(dp)

        return dp[target]