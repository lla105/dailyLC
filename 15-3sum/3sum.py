class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                cursum = nums[i] + nums[l] + nums[r]
                if cursum>0:
                    r-=1
                elif cursum <0:
                    l+=1
                else:
                    output.add( (nums[i],nums[l],nums[r]) )
                    r-=1
                    l+=1

        return list(output)