class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        # nums = [0,2,7,9 ,3 , 1, 0]
        # dp =.  [0,2,7,11,10,12,11]
        nums.insert(0,0)
        dp = [ 0 ] * len(nums)
        dp[1] = nums[1]
        dp[2] = nums[2] 
        for i in range(3, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], nums[i], nums[i]+dp[i-3])
        print(dp)

        return max(dp[-1] , dp[-2])