class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        result2 = []
        nums=sorted(nums)
        def bt(curList, startindex):
            if len(curList)>=len(nums):
                result.add( tuple(curList) )

                return
            result.add( tuple(curList) )
            result2.append( tuple(curList) )
            for i in range(startindex, len(nums)):
                
                bt(curList+[nums[i]] , i+1)
        bt([] , 0)

        return result
