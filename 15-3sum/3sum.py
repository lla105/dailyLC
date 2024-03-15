class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        answers = set()

        for i in range(len(nums)):
            num1 = nums[i]
            j = i+1
            k = len(nums)-1

            while j<k:
                num2 = nums[j]
                num3 = nums[k]
                tempsum = num1+num2+num3

                if tempsum>0:
                    k-=1
                elif tempsum<0:
                    j+=1
                else:
                    answers.add( (num1,num2,num3) )
                    k-=1
                    j+=1
        return answers