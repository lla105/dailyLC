class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target=0
        answers = set()
        nums=sorted(nums)
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                temp = nums[i]+nums[left]+nums[right]
                # print(">>> ",nums[i],nums[left],nums[right],'=',temp)
                if temp ==0:
                    answers.add( (nums[i],nums[left],nums[right]) )
                    left+=1
                    right-=1
                elif temp<=0:
                    left += 1
                else :
                    right -= 1
                # right -= 1
            # print()

        return answers