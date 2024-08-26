class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # self.arr = []
        self.arr = set()
        nums = sorted(nums)
        def bf( curList , index ) :
            # self.arr.append( tuple(curList) ) 
            self.arr.add ( tuple(curList) )
            for i in range( index, len(nums)):
                bf( curList+[nums[i]] , i+1 )

        bf( [] , 0 ) 
        return self.arr