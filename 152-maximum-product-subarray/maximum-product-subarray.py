class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minProd = 1
        maxProd = 1
        dp = [0] * len(nums)

        if nums[-1] ==0 :
            dp[-1] = 0
        else:
            dp[-1] = nums[-1]
            maxProd = nums[-1]
            minProd = maxProd

        for i in range(len(nums)-2, -1, -1):
            res = dp[i+1]
            if nums[i]==0:
                minProd = 1
                maxProd = 1
                dp[i] = res if res>0 else 0
                continue

            temp = maxProd
            maxProd = max(maxProd * nums[i], minProd * nums[i] , nums[i])
            minProd = min(temp * nums[i] , minProd * nums[i] , nums[i])

            res = max(res, maxProd)
            dp[i] = res

        return dp[0]


        # [2, ]