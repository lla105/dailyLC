class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while l < r:
                num1 = nums[i]
                num2 = nums[l]
                num3 = nums[r]
                cursum = num1 + num2 + num3
                # print(cursum, '=', num1,num2,num3)
                if cursum == 0:
                    s.add( (num1,num2,num3) )
                    r -= 1
                    l += 1
                elif cursum > 0 :
                    r -= 1
                else:
                    l += 1
        return s