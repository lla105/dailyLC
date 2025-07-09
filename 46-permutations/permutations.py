class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def traverse( cur_arr, av_list ):
            # print('>> ', av_list)
            if len(cur_arr) == len(nums):
                output.append( cur_arr )
                return
            for i in range( len(av_list)):
                next_av_list = av_list[:i] + av_list[i+1:]
                traverse( cur_arr+[av_list[i]] , next_av_list )
        traverse( [], nums )
        return output

# Decisions: include num, or don't include num (go to next num)
# 123
# [1] 23
#   [1,2] 3
#       [1,2,3]
#   [1,3] 2
#       [1,3,2]
# [2] 13
#   [2,3] 1
#       [2,3,1]
#   [2,1] 3
#       [2,1,3]
# [3]
#   [3,1]
#       [3,1,2]
#   [3,2]
#       [3,2,1]

# 1,2,3
# 1,3,2
# 2,3,1
# 3,1,2
# 3,2,1

# [1,2,3] -> 3*2*1 = 6
# [1,2,3,4] -> 4*3*2 = 24

