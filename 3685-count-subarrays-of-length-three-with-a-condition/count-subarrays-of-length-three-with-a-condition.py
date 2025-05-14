class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        if len(nums) < 3 :
            return 0
        output = 0
        for i in range(len(nums)-2):
            num1 = nums[i]
            num2 = nums[i+1]
            num3 = nums[i+2]
            if (num1+num3) == (num2/2) :
                output += 1
        return output