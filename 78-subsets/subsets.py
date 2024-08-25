class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = set()

        def bf( curList , index ):
            self.result.add( tuple(curList) )
            if len(curList)>=len(nums):
                return
            for i in range(index, len(nums)):
                bf( curList+[nums[i]] , i+1)
        bf([], 0)
        return self.result