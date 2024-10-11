class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        longest = 0
        templongest = 0
        for i in range(len(nums)):
            s.add(nums[i])
        for i in range(len(nums)):
            if nums[i]-1 in s:
                continue
            else:
                templongest = 0
                curnum = nums[i] 
                while curnum in s:
                    templongest += 1
                    curnum+= 1
                longest = max(longest, templongest)
        return longest
        