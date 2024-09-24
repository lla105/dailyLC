class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = set()

        def bf( curList , arr ) :
            if len(curList ) == len(nums) :
                output.add( tuple(curList) )
                return 
            for i in range( len(arr)):
                nextlist = curList + [arr[i]]
                nextarr = arr[:i] + arr[i+1:]
                bf( nextlist , nextarr)

        bf( [] , nums) 
        return output