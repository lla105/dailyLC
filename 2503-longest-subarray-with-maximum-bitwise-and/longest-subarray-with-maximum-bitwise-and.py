class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best = [ 0,0 ] # [ num, maxlength]
        curbest = [0,0]
        maxnum = max(nums)
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == maxnum :
                count += 1
            else:
                maxcount = max(maxcount, count)
                count = 0
        maxcount = max(maxcount, count)
        
        return maxcount