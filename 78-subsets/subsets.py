class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def traverse( nums_index , temp_arr ) :
            if nums_index >= len(nums) :
                output.append( tuple(temp_arr) )

                return
            output.append( tuple(temp_arr) )
            for i in range( nums_index , len(nums) ) :
                traverse( i+1 , temp_arr + [nums[i]] )
        traverse( 0 , [] )
        return output
        
# somefunction( nums_index, temp_arr )
#    check base case

#      for i in range(nums_index , len(nums)):
#           somefunction( i+1 , temp_arr+[nums[i]] ) > (0+1 , [1])

#somefunction(0, [] )
#somefunction(1, [1] )
#somefunction(2, [1,2] )
#somefunction(3, [1,2,3] )
#somefunction(3, [1,3] )

