class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        def traverse(start_index, cur_arr) :
            output.append( cur_arr )

            if start_index == len(nums) :
                return
            for i in range( start_index, len(nums)):
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                traverse( i+1, cur_arr + [nums[i]] )
        traverse(0, [])
        return output