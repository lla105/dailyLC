class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resultset = set()

        def bf( curList , index ):
            resultset.add( tuple(curList) )
            for i in range( index, len(nums)):
                bf( curList+[nums[i]] , i+1)

        bf([], 0)
        return resultset