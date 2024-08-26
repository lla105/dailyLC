class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.arr = set()
        nums = sorted(nums)
        def bf( curList , index ) :
            self.arr.add ( tuple(curList) )
            for i in range( index, len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                bf( curList+[nums[i]] , i+1 )

        bf( [] , 0 ) 
        return self.arr