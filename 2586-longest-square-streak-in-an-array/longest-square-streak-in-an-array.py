class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)

        ogset = set(nums)
        print(ogset)
        output = -1
        for i in range(len(nums)):
            count = 0
            sqrtnum = nums[i]*nums[i]
            while sqrtnum in ogset:
                print( sqrtnum, ' is in ogset ')
                sqrtnum *= sqrtnum
                count += 1
                output = max(output,count)
            
        if output<=0:
            return -1
        else:
            return output+1