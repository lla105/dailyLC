class Solution:
    def solveTAB(self, nums, n):
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]

    def rob(self, nums: List[int]) -> int:

        return self.solveTAB(nums, len(nums))

        # if len(nums)==1:
        #     return nums[0]
        # for i in range(2, len(nums)):
        #     nums[i] += nums[i-2]
        #     # print(nums)

        # return max(nums[-1], nums[-2])