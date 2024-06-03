class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultlist = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i+1
            r = len(nums) -1
            while l<r:
                if nums[i]+nums[l]+nums[r] > 0:
                    r-=1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l+=1
                else:
                    resultlist.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
            
        return resultlist
                