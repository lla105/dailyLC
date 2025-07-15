class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def traverse(cur_arr, av_list , idx):
            # if len(cur_arr) == len(nums) :
            #     output.append( tuple(cur_arr) )
            #     return
            if idx == len(nums) :
                return
            output.append( tuple(cur_arr) )
            for i in range( len(av_list) ) :
                # next_av_list = av_list[:i] + av_list[i+1:]
                next_av_list = av_list[i+1:]
                traverse( cur_arr+[av_list[i]] , next_av_list , idx)
        traverse([] , nums , 0)

        return output

#(cur_arr , av_list)
#([] , [1,2,3])
#   ([])



#[]
#   [1]
#       [1,2]
#           [1,2,3]
#   [2]
#       [2,3]
#   [3]