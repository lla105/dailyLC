class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        cache = [0] * len(nums)
        cache[0] = nums[0]
        cache[1] = nums[1]
        cache[2] = nums[0] + nums[2]
        for i in range( 3, len(nums)):
            one = nums[i] + cache[i-2]
            two = nums[i] + cache[i-3]
            cache[i] = max( one , two )
        print(cache)
        return max( cache[-1] , cache[-2])
        # self.output = 0
        # def traverse(prev_sum, idx):
        #     if idx >=len(nums) :
        #         self.output = max(self.output , prev_sum)
        #         return prev_sum
        #     cur_sum = prev_sum + nums[idx]
        #     one = traverse(cur_sum, idx+2)
        #     two = traverse(cur_sum, idx+3)
        #     three = traverse(prev_sum, idx+1)
        # traverse(0, 0)
        # return self.output

#t(0,0)
#   one = t(2,1)
#       one = t()
#   two = t(2,2)
#   thr = t(0,1)

#nums = [a,b,c,d,e]
#nums = [5,1,1,5,1]
#notes:
# at each num, either:
# - pick current number
#   - pick next next num (i+2)
#   - pick (i+3) num
# - pick next num (i+1)


# [2,7,9,3,1]
#[]
#   [2]2
#       [2,9]11
#           [2,9,1]12
#       [2,3]5
#   [7]7
#       [7,3]10
#       [7,1]8