class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while l<r:
                num1 = nums[i]
                num2 = nums[l]
                num3 = nums[r]
                tempSum = num1+num2+num3
                if tempSum == 0:
                    # result.append((num1,num2,num3))
                    result.add((num1,num2,num3))
                    l+=1
                    r-=1
                elif tempSum >0:
                    r -= 1
                else:
                    l +=1 
        return result