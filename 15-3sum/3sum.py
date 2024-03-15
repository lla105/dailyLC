class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        # result = []
        result = set()

        for i in range(len(nums)):
            num1 = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j<k:
                num2 = nums[j]
                num3 = nums[k]
                currSum = num1 + num2 + num3
                # print(f' {num1} + {num2} + {num3}')
                if currSum > 0:
                    k = k -1
                elif currSum < 0:
                    j = j + 1
                else : 
                    # print("append")
                    result.add( (num1,num2,num3) )
                    k = k - 1
                    j = j + 1
        return result