class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # format { num : index } 
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return (d[diff], i)
            else:
                d[nums[i]] = i
        print('asdf')
        # return