class Solution:
    def findMin(self, nums: List[int]) -> int:
        newnum = []
        restarr = []
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                newnum = nums[i+1:] + nums[0:i+1]

        print(newnum)
        if newnum:
            return newnum[0]
        else:
            return nums[0]
        # l, r = 0, len(nums) - 1

        # while l < r:
        #     m = l + (r - l)

        #     if nums[m] > nums[r]:
        #         l = m + 1
             
        #     else:
        #          r = m 

        # return nums[l]  
        # return 0
