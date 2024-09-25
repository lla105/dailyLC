class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4 :
            return max(nums)
        arr1 = nums[:len(nums)-1]
        arr2 = nums[1:]
        dp1 = [0] * len(arr1)
        dp2 = [0] * len(arr2)
        for i in range(2) :
            dp1[i] = arr1[i]
            dp2[i] = arr2[i]
        for i in range( 2, len(arr1)):
            if i==2:
                dp1[i] = arr1[i]+dp1[i-2]
                dp2[i] = arr2[i]+dp2[i-2]
                continue
            dp1[i] = max( arr1[i]+dp1[i-2] , arr1[i]+dp1[i-3])
            dp2[i] = max( arr2[i]+dp2[i-2] , arr2[i]+dp2[i-3])
        return max( dp1[-1] , dp2[-1], dp1[-2], dp2[-2])