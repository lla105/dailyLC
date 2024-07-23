class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                cursum = nums[i] + nums[l] + nums[r]
                if cursum==0:
                    result.add( (nums[i],nums[l],nums[r]) )
                    r-=1
                    l+=1
                elif cursum>0:
                    r -= 1
                else:
                    l += 1

        return result