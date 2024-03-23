class Solution:
    def helper(self, nums):
        print(">>>", nums)
        dp = [0] * (len(nums)+2)
        # print(dp)
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(nums[i]+dp[i+2] , dp[i+1])
            print(dp)
        return max(dp)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1 = self.helper(nums[1:])
        rob2 = self.helper(nums[:-1])


        return max(rob1, rob2)